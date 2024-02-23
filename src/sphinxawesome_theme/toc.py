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


def findall(node: Node, selection: Node) -> Any:
    """A backwards-compatible method to traverse docutils nodes.

    `findall` isn't available in docutils < 0.18.
    This can be removed if we pin the minimum version of Sphinx to >5.
    """
    findall = "findall" if hasattr(node, "findall") else "traverse"

    return getattr(node, findall)(selection)


def change_toc(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: Node,
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
    for node in findall(toc, nodes.reference):  # type: ignore
        if node["refuri"] == "#":
            # Remove the `list_item` wrapping the `reference` node.
            node.parent.parent.remove(node.parent)

    # Outdent the new empty outer bullet lists
    doc = new_document("<partial node>")
    doc.append(toc)

    # Replace outer bullet lists with inner bullet lists
    for node in findall(doc, nodes.bullet_list):  # type: ignore
        if (
            len(node.children) == 1
            and isinstance(node.next_node(), nodes.list_item)
            and isinstance(node.next_node().next_node(), nodes.bullet_list)
        ):
            doc.replace(node, node.next_node().next_node())

    if hasattr(app.builder, "_publisher"):
        app.builder._publisher.set_source(doc)
        app.builder._publisher.publish()
        context["toc"] = app.builder._publisher.writer.parts["fragment"]
