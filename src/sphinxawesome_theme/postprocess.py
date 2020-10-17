"""Post-process the HTML produced by Sphinx.

Modifications that can be done on the finished HTML
are better done using BeautifulSoup. Here, a simple
pipeline is defined for reading all HTML files,
parsing them with BeautifulSoup and perform a chain
of actions on the tree in place.
See the `_modify_html()` function for the list of
transformations.

Note: If you add elements to the HTML, add traditional
classes instead of using Tailwind's utility classes.
This is because this Python file is not processed by
PurgeCSS.

:copyright: Copyright 2020, Kai Welke.
:license: MIT, see LICENSE.
"""

import os
from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup
from sphinx.application import Config, Sphinx
from sphinx.locale import _
from sphinx.util import logging

from . import __version__

logger = logging.getLogger(__name__)


def _get_html_files(outdir: str) -> List[str]:
    """Get a list of HTML files."""
    html_list = []
    for root, _dirs, files in os.walk(outdir):
        html_list.extend(
            [os.path.join(root, file) for file in files if file.endswith(".html")]
        )
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
    """Add a code copy button to all ``div.highlight`` elements.

    The icon is from the Material Design icon set:
    https://material.io/resources/icons/?icon=content_copy
    """
    for code in tree("div", class_="highlight"):
        # create the button
        btn = tree.new_tag("button", attrs={"class": "copy"})
        btn["aria-label"] = _("Copy this code block")

        # create the SVG icon
        svg = tree.new_tag(
            "svg",
            xmlns="http://www.w3.org/2000/svg",
            viewBox="0 0 24 24",
            fill="currentColor",
        )
        svg["aria-hidden"] = "true"

        # svg path
        path = tree.new_tag(
            "path",
            d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 "
            "4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 "
            "0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z",
        )
        svg.append(path)
        btn.append(svg)
        code.append(btn)


def _add_external_link_icon(tree: BeautifulSoup) -> None:
    """Add icon to all ``a.external`` elements.

    The icon is from the Materials icons set:
    https://material.io/resources/icons/?icon=open_in_new
    """
    for link in tree("a", class_="external"):
        # create the icon
        svg = tree.new_tag(
            "svg",
            attrs={
                "xmlns": "http://www.w3.org/2000/xvg",
                "viewBox": "0 0 24 24",
                "class": "external-link-icon",
                "fill": "currentColor",
            },
        )
        svg["aria-hidden"] = "true"
        # svg path
        path = tree.new_tag(
            "path",
            d="M19 19H5V5h7V3H5a2 2 0 00-2 2v14a2 2 0 002 2h14c1.1 0 "
            "2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z",
        )
        svg.append(path)
        link.append(svg)


def _collapsible_nav(tree: BeautifulSoup) -> None:
    """Restructure the navigation links to make them collapsible.

    First, all links in the navigation sidebar are wrapped in a ``div``.
    This allows them to be 'block' and 'position relative' for the
    'expand' icon to be positioned against.

    Second, an icon is inserted right before the link.
    Adding the icon as separate DOM element allows click events to be
    captured separately between the icon and the link.

    The icon is from the Materials icons set:
    https://material.io/resources/icons/?icon=chevron_right
    """
    for link in tree.select(".nav-toc a"):
        # First, all links should be wrapped in a div.nav-link
        link.wrap(tree.new_tag("div", attrs={"class": "nav-link"}))
        # Next, insert a span.expand before the link, if the #nav-link
        # has any sibling elements (a ``ul`` in the navigation menu)
        if link.parent.next_sibling:
            # create the icon
            svg = tree.new_tag(
                "svg",
                attrs={
                    "xmlns": "http://www.w3.org/2000/xvg",
                    "viewBox": "0 0 24 24",
                    "class": "expand",
                    "fill": "currentColor",
                },
            )
            path = tree.new_tag(
                "path", d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"
            )
            svg.append(path)
            link.insert_before(svg)


def _divs_to_section(tree: BeautifulSoup) -> None:
    """Convert ``div.section`` to semantic ``section`` elements.

    With docutils 0.17, this should not be necessary anymore.
    """
    for div in tree("div", class_="section"):
        div.name = "section"
        del div["class"]


def _divs_to_figure(tree: BeautifulSoup) -> None:
    """Convert ``div.figure`` to semantic ``figure`` elements.

    With docutils 0.17, this should not be necessary anymore.
    """
    for div in tree("div", class_="figure"):
        div.name = "figure"
        div["class"].remove("figure")
        caption = div.find("p", class_="caption")
        if caption:
            caption.name = "figcaption"
            del caption["class"]


def _expand_current(tree: BeautifulSoup) -> None:
    """Add the ``.expanded`` class to li.current elements."""
    for li in tree("li", class_="current"):
        li["class"] += ["expanded"]


def _remove_pre_spans(tree: BeautifulSoup) -> None:
    """Remove unnecessarily nested ``span.pre`` elements in inline ``code``."""
    for code in tree("code"):
        for span in code("span", class_="pre"):
            span.unwrap()


def _remove_xref_spans(tree: BeautifulSoup) -> None:
    """Remove unnecessarily nested ``span.std-ref`` elements in cross-references."""
    for link in tree("a"):
        for span in link("span", class_="std-ref"):
            span.unwrap()


def _modify_html(html_filename: str, config: Config) -> None:
    """Modify a single HTML document.

    The HTML document is parsed into a BeautifulSoup tree.

    The modifications are performed in order and in place.

    After these modifications, the HTML is written into a file,
    overwriting the original file.
    """
    with open(html_filename) as html:
        tree = BeautifulSoup(html, "html.parser")

    _divs_to_section(tree)
    _divs_to_figure(tree)
    _expand_current(tree)
    _collapsible_nav(tree)
    _wrap_literal_blocks(tree)
    _add_copy_button(tree)
    if config.mark_external_links:
        _add_external_link_icon(tree)
    _remove_pre_spans(tree)
    _remove_xref_spans(tree)

    with open(html_filename, "w") as out_file:
        out_file.write(str(tree))


def post_process_html(app: Sphinx, exc: Optional[Exception]) -> None:
    """Perform modifications on the HTML after building.

    This is an extra function, that gets a list from all HTML
    files in the output directory, then runs the ``_modify_html``
    function on each of them.
    """
    if app.builder.name not in ["html", "dirhtml"]:
        return

    if exc is None:
        html_files = _get_html_files(app.outdir)

        for doc in html_files:
            _modify_html(doc, app.config)


def setup(app: "Sphinx") -> Dict[str, Any]:
    """Set this up as internal extension."""
    app.add_config_value("mark_external_links", True, "env")
    app.connect("build-finished", post_process_html)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
