"""Post-process the HTML produced by Sphinx.

- wrap literal blocks in `div.highlights` in order to
- inject copy code buttons

:copyright: Copyright 2020, Kai Welke.
:license: MIT, see LICENSE.
"""

import os
from typing import List

from bs4 import BeautifulSoup
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)


def _get_html_files(outdir: str) -> List[str]:
    """Get a list of HTML files."""
    html_list = []
    for root, _, files in os.walk(outdir):
        for file in files:
            if file.endswith(".html"):
                html_list.append(os.path.join(root, file))
    return html_list


def _wrap_literal_blocks(tree: BeautifulSoup) -> None:
    """Wrap literal blocks in ``div.highlight`` elements.

    This allows us to add 'copy code' buttons to all ``div.highlight``
    elements.
    """
    literal_blocks = tree("pre", class_="literal-block")

    [
        block.wrap(tree.new_tag("div", attrs={"class": "highlight"}))
        for block in literal_blocks
    ]


def _add_copy_button(tree: BeautifulSoup) -> None:
    """Add code copy button to all ``div.highlight`` elements."""
    code_blocks = tree("div", class_="highlight")

    for code in code_blocks:
        # create the button
        btn = tree.new_tag("button", attrs={"class": "copy"})
        btn["aria-label"] = "Copy this code block"

        # create the SVG icon
        svg = tree.new_tag(
            "svg", xmlns="http://www.w3.org/2000/svg", viewBox="0 0 20 20"
        )
        svg["aria-hidden"] = "true"

        # svg path
        path = tree.new_tag(
            "path",
            d="M6 6V2c0-1.1.9-2 2-2h10a2 2 0 012 2v10a2 2 0 01-2 2h-4v4a2 2 0 "
            "01-2 2H2a2 2 0 01-2-2V8c0-1.1.9-2 2-2h4zm2 0h4a2 2 0 012 "
            "2v4h4V2H8v4zM2 8v10h10V8H2z",
        )
        svg.append(path)
        btn.append(svg)
        code.append(btn)


def _collapsible_nav(tree: BeautifulSoup) -> None:
    """Add small triangle icons to the links in the navigation.

    Adding them as spans instead of ``:after`` allows to capture
    click events on the link and the expand icon separately.
    """
    nav_links = tree.select("nav ul a")

    for link in nav_links:
        # ignore 'leaf' nodes
        if link.next_sibling:
            span = tree.new_tag("span", attrs={"class": "expand"})
            span.string = "\u25be"
            link.insert_after(span)


def _divs_to_section(tree: BeautifulSoup) -> None:
    """Convert ``div.section`` to proper ``section``.

    With docutils 0.17, this should not be necessary anymore
    and can be removed.
    """
    divs = tree("div", class_="section")
    for div in divs:
        div.name = "section"
        del div["class"]


def _expand_current(tree: BeautifulSoup) -> None:
    """Add the ``.expanded`` class to li.current elements."""
    for li in tree("li", class_="current"):
        li["class"] += ["expanded"]
        for sub in li("li", class_="toctree-l2"):
            sub["class"] += ["expanded"]


def _modify_html(html_filename: str) -> None:
    """Modify a single HTML document.

    - Parse the HTML document into a tree
    - Perform the modifications on the tree in place
    - Write out the tree as new HTML document (with the same filename)
    """
    with open(html_filename) as html:
        tree = BeautifulSoup(html, "html.parser")

    _divs_to_section(tree)
    _expand_current(tree)
    _collapsible_nav(tree)
    _wrap_literal_blocks(tree)
    _add_copy_button(tree)

    with open(html_filename, "w") as out_file:
        out_file.write(tree.prettify(formatter="html5"))


def post_process_html(app: Sphinx, exc: Exception) -> None:
    """Perform modifications on the built HTML."""
    if exc is None:
        html_files = _get_html_files(app.outdir)

        for doc in html_files:
            _modify_html(doc)
