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
from sphinx.application import Sphinx
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
        # Don't add the nav-link class twice (#166)
        if "nav-link" not in link.parent.get("class", []):
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


def _expand_current(tree: BeautifulSoup) -> None:
    """Add the ``.expanded`` class to li.current elements."""
    for li in tree("li", class_="current"):
        if "expanded" not in li.get("class", []):
            li["class"] += ["expanded"]


def _modify_html(html_filename: str) -> None:
    """Modify a single HTML document.

    The HTML document is parsed into a BeautifulSoup tree.

    The modifications are performed in order and in place.

    After these modifications, the HTML is written into a file,
    overwriting the original file.
    """
    with open(html_filename) as html:
        tree = BeautifulSoup(html, "html.parser")

    _expand_current(tree)
    _collapsible_nav(tree)

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
            _modify_html(doc)


def setup(app: "Sphinx") -> Dict[str, Any]:
    """Set this up as internal extension."""
    app.add_config_value("mark_external_links", True, "env")
    app.connect("build-finished", post_process_html)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
