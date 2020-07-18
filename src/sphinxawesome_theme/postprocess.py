"""Post-process the HTML produced by Sphinx.

- wrap literal blocks in `div.highlights` in order to
- inject copy code buttons

Note: The security warning S410 is about unsafe XML parsing.
Since we don't really parse external XML data here,
it maybe ok to ignore for now.

:copyright: Copyright 2020, Kai Welke.
:license: MIT, see LICENSE.
"""

import os
from typing import List

from lxml import etree, html  # noqa: S410
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)


def _copy_icon() -> etree.Element:
    """Generate an SVG with the copy icon."""
    svg = etree.Element("svg")
    svg.set("xmlns", "http://www.w3.org/2000/svg")
    svg.set("aria-hidden", "true")
    svg.set("viewBox", "0 0 20 20")
    path = etree.SubElement(svg, "path")
    path.set(
        "d",
        "M6 6V2c0-1.1.9-2 2-2h10a2 2 0 012 2v10a2 2 0 01-2 2h-4v4a2 2 0 "
        "01-2 2H2a2 2 0 01-2-2V8c0-1.1.9-2 2-2h4zm2 0h4a2 2 0 012 "
        "2v4h4V2H8v4zM2 8v10h10V8H2z",
    )
    return svg


def _get_html_files(outdir: str) -> List[str]:
    """Get a list of HTML files."""
    html_list = []
    for root, _, files in os.walk(outdir):
        for file in files:
            if file.endswith(".html"):
                html_list.append(os.path.join(root, file))
    return html_list


def _wrap_literal_blocks(tree: etree._ElementTree) -> None:
    """Wrap literal blocks in ``div.highlight`` elements."""
    literal_blocks = tree.xpath("//pre[@class='literal-block']")

    for block in literal_blocks:
        div = etree.Element("div")
        div.set("class", "highlight")
        block.addprevious(div)
        div.insert(0, block)


def _add_copy_button(tree: etree._ElementTree) -> None:
    """Add code copy button to all ``div.highlight`` elements."""
    code_blocks = tree.xpath("//div[@class='highlight']")

    for code in code_blocks:
        btn = etree.Element("button")
        btn.set("aria-label", "Copy this code block")
        btn.set("class", "copy")
        btn.append(_copy_icon())
        code.insert(0, btn)


def _modify_html(html_filename: str) -> None:
    """Parse and modify a HTML document."""
    tree = html.parse(html_filename)

    _wrap_literal_blocks(tree)
    _add_copy_button(tree)

    with open(html_filename, "wb") as out_file:
        tree.write(out_file, method="c14n")


def post_process_html(app: Sphinx, exc: Exception) -> None:
    """Perform modifications on the built HTML."""
    if exc is None:
        html_files = _get_html_files(app.outdir)

        for doc in html_files:
            _modify_html(doc)
