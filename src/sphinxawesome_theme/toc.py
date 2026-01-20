"""Manipulate the on-page TOC.

:copyright: Kai Welke.
:license: MIT
"""

from __future__ import annotations

from typing import Any

from docutils import nodes
from docutils.nodes import Node
from sphinx.application import Sphinx
from sphinx.environment.adapters.toctree import TocTree
from sphinx.util.docutils import new_document


def change_toc(
    app: Sphinx,
    pagename: str,
    _templatename: str,
    context: dict[str, Any],
    _doctree: Node,
) -> None:
    """Change the way the `{{ toc }}` helper works.

    By default, Sphinx includes the page title in the on-page TOC.
    We don't want that.

    Sphinx returns the following structure:

    <ul>
        <li><a href="#">Page title</a></li>
        <ul>
            <li><a href="#anchor">H2 and below</a></li>
        </ul>
    </ul>

    We first remove the `title` node. This gives us:

    <ul>
        <ul>
            <li><a href="#anchor">H2 and below</a></li>
        </ul>
    </ul>

    Then, we _outdent_ the tree.
    """
    toc = TocTree(app.builder.env).get_toc_for(pagename, app.builder)

    # Remove `h1` node
    for node in toc.findall(nodes.reference):
        if node["refuri"] == "#":
            # Remove the `list_item` wrapping the `reference` node.
            node.parent.parent.remove(node.parent)

    # Outdent the new empty outer bullet lists
    doc = new_document("<partial node>")
    doc.append(toc)

    # Replace outer bullet lists with inner bullet lists
    for node in doc.findall(nodes.bullet_list):
        if (
            len(node.children) == 1
            and isinstance(node.next_node(), nodes.list_item)
            and isinstance(node.next_node().next_node(), nodes.bullet_list)  # type:ignore
        ):
            doc.replace(node, node.next_node().next_node())  # type:ignore

    toc_root = doc.children[0] if doc.children else None

    # Use the public builder API to render the doctree fragment.
    context["toc"] = app.builder.render_partial(toc_root)["fragment"]  # type: ignore[attr-defined]
