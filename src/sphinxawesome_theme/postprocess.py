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
from __future__ import annotations

import os
import re
from typing import Any

from bs4 import BeautifulSoup, Comment
from sphinx.application import Sphinx
from sphinx.util import logging

from . import __version__, icons, logos

logger = logging.getLogger(__name__)


def _get_html_files(outdir: str) -> list[str]:
    """Get a list of HTML files."""
    html_list = []
    for root, _, files in os.walk(outdir):
        html_list.extend(
            [os.path.join(root, file) for file in files if file.endswith(".html")]
        )
    return html_list


def _collapsible_nav(tree: BeautifulSoup) -> None:
    """Make navigation links with children collapsible."""
    for link in tree.select("#left-sidebar a"):
        # Check if the link has "children"
        children = link.next_sibling
        if children and children.name == "ul":
            # State must be available in the link and the list
            li = link.parent
            li[
                "x-data"
            ] = "{ expanded: $el.classList.contains('current') ? true : false }"
            link["@click"] = "expanded = !expanded"
            # The expandable class is a hack because we can't use Tailwind
            # I want to have _only_ expandable links with `justify-between`
            link["class"].append("expandable")
            link[":class"] = "{ 'expanded' : expanded }"
            children["x-show"] = "expanded"

            # Create a button with an icon inside to get focus behavior
            button = tree.new_tag(
                "button",
                attrs={"type": "button", "@click.prevent.stop": "expanded = !expanded"},
            )
            label = tree.new_tag("span", attrs={"class": "sr-only"})
            button.append(label)

            # create the icon
            svg = BeautifulSoup(icons.ICONS["chevron_right"], "html.parser").svg
            button.append(svg)
            link.append(button)


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
    """Make headerlinks copy their URL on click."""
    for link in tree("a", class_="headerlink"):
        link["@click.prevent"] = "window.navigator.clipboard.writeText($el.href)"
        del link["title"]
        link["aria-label"] = "Copy link to this element"
        link["data-tooltip"] = "Copy link to this element"


def _scrollspy(tree: BeautifulSoup) -> None:
    """Add an active class to current TOC links in the right sidebar."""
    for link in tree("a", class_="headerlink"):
        if link.parent.name in ["h2", "h3"] or (
            link.parent.name == "dt" and "sig" in link.parent["class"]
        ):
            active_link = link["href"]
            link[
                "x-intersect.margin.0%.0%.-70%.0%"
            ] = f"activeSection = '{active_link}'"

    for link in tree.select("#right-sidebar a"):
        active_link = link["href"]
        link[":data-current"] = f"activeSection === '{active_link}'"


def _external_links(tree: BeautifulSoup) -> None:
    """Add `rel="nofollow noopener"` to external links.

    The alternative was to copy `visit_reference` in the HTMLTranslator
    and change literally one line.
    """
    for link in tree("a", class_="reference external"):
        link["rel"] = "nofollow noopener"
        # append icon
        link.append(BeautifulSoup(icons.ICONS["external_link"], "html.parser").svg)


def _strip_comments(tree: BeautifulSoup) -> None:
    """Remove HTML comments from documents."""
    comments = tree.find_all(string=lambda text: isinstance(text, Comment))
    for c in comments:
        c.extract()


def _code_headers(tree: BeautifulSoup) -> None:
    """Add the programming language to a code block."""
    # Find all "<div class="highlight-<LANG> notranslate>" blocks
    pattern = re.compile("highlight-(.*) ")
    for code_block in tree.find_all("div", class_=pattern):
        hl_lang = None
        # Get the highlight language
        classes_string = " ".join(code_block.get("class", []))
        match = pattern.search(classes_string)
        if match:
            hl_lang = match.group(1).replace("default", "python")

        parent = code_block.parent

        # Deal with code blocks with captions
        if "literal-block-wrapper" in parent.get("class", []):
            caption = parent.select(".code-block-caption")[0]
            if caption:
                span = tree.new_tag("span", attrs={"class": "code-lang"})
                span.append(tree.new_string(hl_lang))
                caption.insert(0, span)
        else:
            # Code block without captions, we need to wrap them first
            wrapper = tree.new_tag("div", attrs={"class": "literal-block-wrapper"})
            caption = tree.new_tag("div", attrs={"class": "code-block-caption"})
            span = tree.new_tag("span", attrs={"class": "code-lang"})
            span.append(tree.new_string(hl_lang))
            caption.append(span)
            code_block.wrap(wrapper)
            wrapper.insert(0, caption)


def _modify_html(html_filename: str, app: Sphinx) -> None:
    """Modify a single HTML document.

    1. The HTML document is parsed into a BeautifulSoup tree.
    2. The modifications are performed in order and in place.
    3. After these modifications, the HTML is written into a file,
    overwriting the original file.
    """
    with open(html_filename, encoding="utf-8") as html:
        tree = BeautifulSoup(html, "html.parser")

    theme_options = logos.get_theme_options(app)

    _collapsible_nav(tree)
    if theme_options.get("awesome_external_links"):
        _external_links(tree)
    _remove_empty_toctree(tree)
    _scrollspy(tree)
    if theme_options.get("awesome_header_links"):
        _headerlinks(tree)
    if app.config.html_awesome_code_headers:
        _code_headers(tree)
    _strip_comments(tree)

    with open(html_filename, "w", encoding="utf-8") as out_file:
        out_file.write(str(tree))


def post_process_html(app: Sphinx, exc: Exception | None) -> None:
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


def setup(app: Sphinx) -> dict[str, Any]:
    """Set this up as internal extension."""
    app.connect("build-finished", post_process_html)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
