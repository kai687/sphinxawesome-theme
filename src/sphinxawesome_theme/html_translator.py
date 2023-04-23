"""Modification of the Sphinx HTML5 translator.

Overwrite several methods to improve the HTML output.
This HTML translator is active for the ``html`` and ``dirhtml`` builders.

Code blocks
   The handling of code blocks is modified. Code blocks have a ``header``
   section that displays the highlighting language.
   The caption is also shown in the header.

Code definition lists
   Definitions for ``autodoc`` codes get a ``expand`` button.

:copyright: Copyright Kai Welke.
:license: MIT, see LICENSE for details.
"""
import re
from typing import Any, Dict

from docutils import nodes
from docutils.nodes import Element
from sphinx.application import Sphinx
from sphinx.util import logging
from sphinx.writers.html5 import HTML5Translator

from . import __version__
from .icons import ICONS

logger = logging.getLogger(__name__)


class AwesomeHTMLTranslator(HTML5Translator):
    """Override a few methods to improve the usability."""

    def visit_caption(self: "AwesomeHTMLTranslator", node: Element) -> None:
        """Code block captions."""
        if isinstance(node.parent, nodes.container) and node.parent.get(
            "literal_block"
        ):
            self.body.append(self.starttag(node, "span", "", CLASS="caption-text"))
        else:
            super().visit_caption(node)

    def visit_desc(self: "AwesomeHTMLTranslator", node: Element) -> None:
        """Add a class ``code-definition`` to definition lists.

        For code objects, like functions, classes, methods, etc.
        to distinguish them from regular definition lists.
        """
        cl = node["objtype"] + " code-definition"
        self.body.append(self.starttag(node, "dl", CLASS=cl))

    def visit_desc_inline(self: "AwesomeHTMLTranslator", node: Element) -> None:
        """Change `span` to `code`."""
        self.body.append(self.starttag(node, "code", ""))

    def depart_desc_inline(self: "AwesomeHTMLTranslator", node: Element) -> None:
        """Change `span` to `code`."""
        self.body.append("</code>")

    def visit_desc_name(self: "AwesomeHTMLTranslator", node: Element) -> None:
        """Change `span` to `code`."""
        self.body.append(self.starttag(node, "code", ""))

    def depart_desc_name(self: "AwesomeHTMLTranslator", node: Element) -> None:
        """Change `span` to `code`."""
        self.body.append("</code>")

    def visit_desc_addname(self: "AwesomeHTMLTranslator", node: Element) -> None:
        """Change `span` to `code`."""
        self.body.append(self.starttag(node, "code", ""))

    def depart_desc_addname(self: "AwesomeHTMLTranslator", node: Element) -> None:
        """Change `span` to `code`."""
        self.body.append("</code>")

    def visit_literal_block(self: "AwesomeHTMLTranslator", node: Element) -> None:
        """Overwrite code blocks.

        All code blocks have a header showing the highlighting language
        and an optional caption.
        """
        if node.rawsource == node.astext():
            # node doens't have markup, highlight it!
            lang = node.get("language", "default")
            linenos = node.get("linenos", False)
            highlight_args = node.get("highlight_args", {})
            highlight_args["force"] = node.get("force", False)
            opts = self.config.highlight_options.get(lang, {})

            if linenos and self.config.html_codeblock_linenos_style:
                linenos = "inline"

            highlighted = self.highlighter.highlight_block(
                node.rawsource,
                lang,
                opts=opts,
                linenos=linenos,
                location=node,
                **highlight_args,
            )

            # wrap `placeholder` strings with `<var>` elements.
            # this follows Google's recommendations
            # https://developers.google.com/style/placeholders

            if "hl_text" in highlight_args:
                for placeholder in highlight_args["hl_text"].split(","):
                    placeholder = placeholder.strip()
                    highlighted = re.sub(
                        placeholder,
                        f"<var>{placeholder}</var>",
                        highlighted,
                    )

            # Code blocks without captions aren't wrapped inside a <container>
            # So we add the header here. With captions, see: visit_caption
            if not (
                isinstance(node.parent, nodes.container)
                and node.parent.get("literal_block")
            ):
                attrs = {"data-controller": "code"}
                starttag = self.starttag(
                    node, "div", suffix="", CLASS="code-wrapper", **attrs
                )
                self.body.append(starttag)

                if self.config.html_awesome_code_headers:
                    code_header = "<div class='code-header'>\n"
                    code_header += f"<span class='code-lang'>{lang}</span>"
                    code_header += "</div>\n"
                    self.body.append(code_header)

            # wrap the highlighted string in a div
            self.body.append(highlighted)

            if not (
                isinstance(node.parent, nodes.container)
                and node.parent.get("literal_block")
            ):
                self.body.append("</div>\n")
            # we already included everything here in the `highlighted` string,
            # so we need to skip further processing
            raise nodes.SkipNode
        else:
            # node has markup, it's a samp directive or parsed-literal
            self.body.append("<pre><code>")

    def depart_literal_block(self: "AwesomeHTMLTranslator", node: Element) -> None:
        """Close literal blocks.

        Provide the closing tag for non-highlighted code blocks.
        This method is skipped with ``raise nodes.SkipNode``
        for highlighted code blocks.
        """
        self.body.append("</code></pre>\n")

    def visit_container(self: "AwesomeHTMLTranslator", node: Element) -> None:
        """Overide for code blocks with captions."""
        if node.get("literal_block"):
            node.html5tagname = "div"  # type: ignore[attr-defined]
            attrs = {"data-controller": "code"}
            self.body.append(
                self.starttag(node, node.html5tagname, CLASS="code-wrapper", **attrs)
            )
            lang = node.get("language", "")
            # in the container, `code-header` also contains the caption
            code_header = "<div class='code-header'>\n"
            if self.config.html_awesome_code_headers:
                code_header += (
                    "<span class='code-lang'>"
                    f"{lang.replace('default', 'python')}"
                    "</span>\n"
                )
            self.body.append(code_header)
        else:
            super().visit_container(node)

    def depart_reference(self: "AwesomeHTMLTranslator", node: Element) -> None:
        """Add external link icon."""
        if "refuri" in node and not node.get("internal"):
            self.body.append(ICONS["external_link"])
        super().depart_reference(node)

    def visit_emphasis(self: "AwesomeHTMLTranslator", node: Element) -> None:
        """Change tags for emphasized literals.

        Google recommends using ``<var>`` tags inside ``<code>`` tags
        for placeholders.

        https://developers.google.com/style/placeholders
        """
        if isinstance(node.parent, nodes.literal):
            self.body.append(self.starttag(node, "var", ""))
        else:
            super().visit_emphasis(node)

    def depart_emphasis(self: "AwesomeHTMLTranslator", node: Element) -> None:
        """Change closing tag for emphasized literals."""
        if isinstance(node.parent, nodes.literal):
            self.body.append("</var>")
        else:
            super().depart_emphasis(node)


def setup(app: "Sphinx") -> Dict[str, Any]:
    """Use the AwesomeHTMLTranslator for the html and dirhtml builders.

    This function makes this available as extension.
    """
    # Undo `myst-parser` 0.19 override
    from docutils.writers.html5_polyglot import HTMLTranslator as DUTranslator

    app.add_node(
        nodes.container,
        override=True,
        html=(
            AwesomeHTMLTranslator.visit_container,
            DUTranslator.depart_container,
        ),
    )
    app.set_translator("html", AwesomeHTMLTranslator)
    app.set_translator("dirhtml", AwesomeHTMLTranslator)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
