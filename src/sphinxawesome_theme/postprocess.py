"""Post-process the HTML produced by Sphinx.

- wrap literal blocks in ``div.highlights`` in order to
- inject copy code buttons
- inject HTML for collapsible navigation links
- introduce semantic markup:
  - div.section -> section
  - div.figure -> figure

:copyright: Copyright 2020, Kai Welke.
:license: MIT, see LICENSE.
"""

import os
from typing import List

from bs4 import BeautifulSoup
from sphinx.application import Sphinx
from sphinx.locale import _
from sphinx.util import logging

logger = logging.getLogger(__name__)


def _get_html_files(outdir: str) -> List[str]:
    """Get a list of HTML files."""
    html_list = []
    for root, _dirs, files in os.walk(outdir):
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
    for code in tree("div", class_="highlight"):
        # create the button
        btn = tree.new_tag("button", attrs={"class": "copy"})
        btn["aria-label"] = _("Copy this code block")

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
    for link in tree.select("nav ul a"):
        # ignore 'leaf' nodes
        if link.next_sibling:
            span = tree.new_tag("span", attrs={"class": "expand"})
            span.string = "\u25be"
            link.insert_after(span)


def _divs_to_section(tree: BeautifulSoup) -> None:
    """Convert ``div.section`` to semantic ``section`` elements.

    With docutils 0.17, this should not be necessary anymore.
    """
    for div in tree("div", class_="section"):
        div.name = "section"
        del div["class"]


def _add_focus_to_headings(tree: BeautifulSoup) -> None:
    """Transform headlines so that they can receive focus.

    Sphinx has a default structure of:
    <h1>Title<a class="headerlink" href="...">#</a></h1>

    What I want is:
    <h1><a href="...">Title</a><a class="headerlink" href="...">#</a></h1>

    This allows the headings to receive focus with the TAB key, as well as
    allow logic to be applied on the headerlink '#' (click to copy).
    Keyboard users can just use Ctrl+C on the focussed heading to achieve
    the same goal.
    """
    for heading in tree.select(
        "main h1, main h2, main h3, main h4, main h5, main h6, .admonition-title"
        "figcaption,.code-block-caption, table caption"
    ):
        headerlink = heading.find("a", class_="headerlink")
        caption_text = heading.find("span", class_="caption_text")
        # figures, tables, code blocks
        if caption_text:
            caption_text.wrap(tree.new_tag("a", href=headerlink["href"]))
        # hN, admonitions
        else:
            heading.contents[0].wrap(tree.new_tag("a", href=headerlink["href"]))


def _divs_to_figure(tree: BeautifulSoup) -> None:
    """Convert ``div.figure`` to semantic ``figure`` elements.

    With docutils 0.17, this should not be necessary anymore.
    """
    for div in tree("div", class_="figure"):
        div.name = "figure"
        div["class"].remove("figure")
        caption = div("p", class_="caption")[0]
        caption.name = "figcaption"
        del caption["class"]


def _expand_current(tree: BeautifulSoup) -> None:
    """Add the ``.expanded`` class to li.current elements."""
    for li in tree("li", class_="current"):
        li["class"] += ["expanded"]
        #  for sub in li("li", class_="toctree-l2"):
        #  sub["class"] += ["expanded"]


def _remove_pre_spans(tree: BeautifulSoup) -> None:
    """Remove unnecessary nested ``span.pre`` elements in ``code."""
    for code in tree("code"):
        # we don't need classes for inline code elements
        del code["class"]
        for span in code("span", class_="pre"):
            span.unwrap()


def _modify_html(html_filename: str) -> None:
    """Modify a single HTML document.

    - Parse the HTML document into a tree
    - Perform the modifications on the tree in place
    - Write out the tree as new HTML document (with the same filename)
    """
    with open(html_filename) as html:
        tree = BeautifulSoup(html, "html.parser")

    _divs_to_section(tree)
    _divs_to_figure(tree)
    _expand_current(tree)
    _collapsible_nav(tree)
    _wrap_literal_blocks(tree)
    _add_copy_button(tree)
    _add_focus_to_headings(tree)
    _remove_pre_spans(tree)

    with open(html_filename, "w") as out_file:
        out_file.write(str(tree))


def post_process_html(app: Sphinx, exc: Exception) -> None:
    """Perform modifications on the built HTML."""
    if exc is None:
        html_files = _get_html_files(app.outdir)

        for doc in html_files:
            _modify_html(doc)
