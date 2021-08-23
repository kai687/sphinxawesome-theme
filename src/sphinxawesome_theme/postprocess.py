"""Post-process the HTML produced by Sphinx.

Some modifications can be done more easily on the finished HTML.

This module defines a simple pipeline:

1. Read all HTML files
2. Parse them with `BeautifulSoup`
3. Perform a chain of actions on the tree in place

See the `_modify_html()` function for the list of
transformations.

Note: This file is not processed by Webpack; don't use Tailwind utility classes.
They might not show up in the final CSS.

:copyright: Copyright Kai Welke.
:license: MIT, see LICENSE.
"""

import os
from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Comment
from sphinx.application import Sphinx
from sphinx.util import logging

from . import __version__
from .icons import ICONS

logger = logging.getLogger(__name__)


def _get_html_files(outdir: str) -> List[str]:
    """Get a list of HTML files."""
    html_list = []
    for root, _, files in os.walk(outdir):
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
    """
    for link in tree.select(".nav-toc a"):
        link["data-action"] = "click->sidebar#close"
        # Don't add the nav-link class twice (#166)
        if "nav-link" not in link.parent.get("class", []):
            # First, all links should be wrapped in a div.nav-link
            link.wrap(tree.new_tag("div", attrs={"class": "nav-link"}))
            # Next, insert a span.expand before the link, if the #nav-link
            # has any sibling elements (a ``ul`` in the navigation menu)
            if link.parent.next_sibling:
                # create the icon
                svg = BeautifulSoup(ICONS["chevron_right"], "html.parser").svg
                svg["tabindex"] = "0"
                svg["class"] = ["expand"]
                svg[
                    "data-action"
                ] = "click->sidebar#expand keydown->sidebar#expandKeyPressed"
                link.insert_before(svg)


def _expand_current(tree: BeautifulSoup) -> None:
    """Add the ``.expanded`` class to li.current elements."""
    for li in tree("li", class_="current"):
        if "expanded" not in li.get("class", []):
            li["class"] += ["expanded"]


def _remove_span_pre(tree: BeautifulSoup) -> None:
    """Unwrap unnecessary spans.

    This gets added by visit_Text(). If I overwrite it there,
    it's 20 lines of code for only 1 line of change.
    """
    for span in tree("span", class_="pre"):
        span.unwrap()


def _remove_empty_toctree(tree: BeautifulSoup) -> None:
    """Remove empty toctree divs.

    If you include a `toctree` with the `hidden` option,
    an empty `div` is inserted. Remove them.
    The empty `div` contains a single `end-of-line` character.
    """
    for div in tree("div", class_="toctree-wrapper"):
        children = list(div.children)
        if len(children) == 1 and not children[0].strip():
            div.extract()


def _headerlinks(tree: BeautifulSoup) -> None:
    """Enhance the headerlink experience."""
    for link in tree("a", class_="headerlink"):
        link["data-controller"] = "clipboard"
        link["data-action"] = "click->clipboard#copyHeaderLink"
        link["aria-label"] = "Click to copy this link"
        del link["title"]
        link["class"].extend(["tooltipped", "tooltipped-ne"])


def _external_links(tree: BeautifulSoup) -> None:
    """Add `rel="nofollow noopener"` to external links."""
    for link in tree("a", class_="reference external"):
        link["rel"] = "nofollow noopener"


def _strip_comments(tree: BeautifulSoup) -> None:
    """Remove HTML comments from documents."""
    comments = tree.find_all(string=lambda text: isinstance(text, Comment))
    for c in comments:
        c.extract()


def _modify_html(html_filename: str, app: Sphinx) -> None:
    """Modify a single HTML document.

    1. The HTML document is parsed into a BeautifulSoup tree.
    2. The modifications are performed in order and in place.
    3. After these modifications, the HTML is written into a file,
    overwriting the original file.
    """
    with open(html_filename, encoding="utf-8") as html:
        tree = BeautifulSoup(html, "html.parser")

    _expand_current(tree)
    _collapsible_nav(tree)
    _remove_span_pre(tree)
    _remove_empty_toctree(tree)
    _external_links(tree)
    if app.config.html_awesome_headerlinks:
        _headerlinks(tree)
    _strip_comments(tree)

    with open(html_filename, "w") as out_file:
        out_file.write(str(tree))


def post_process_html(app: Sphinx, exc: Optional[Exception]) -> None:
    """Perform modifications on the HTML after building.

    This is an extra function, that gets a list from all HTML
    files in the output directory, then runs the ``_modify_html``
    function on each of them.
    """
    if app.builder is not None and app.builder.name not in ["html", "dirhtml"]:
        return

    if exc is None:
        html_files = _get_html_files(app.outdir)

        for doc in html_files:
            _modify_html(doc, app)


def setup(app: "Sphinx") -> Dict[str, Any]:
    """Set this up as internal extension."""
    app.connect("build-finished", post_process_html)
    app.add_config_value("html_awesome_headerlinks", True, "html")

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
