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
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.util import logging
from sphinx.writers.html5 import HTML5Translator

from . import __version__
from .icons import ICONS

logger = logging.getLogger(__name__)

EXPAND_MORE_BUTTON = (
    "<button class='expand-more tooltipped tooltipped-nw' "
    "aria-label='Expand this section' aria-expanded='false' "
    f"data-action='collapsible#expandMore'>{ICONS['expand_more']}</button>"
)


class AwesomeHTMLTranslator(HTML5Translator):
    """Override a few methods to improve the usability."""

    def visit_caption(self, node: Element) -> None:
        """Use semantic elements."""
        if isinstance(node.parent, nodes.figure):
            self.body.append("<figcaption>")
            self.add_fignumber(node.parent)
            self.body.append(self.starttag(node, "span", "", CLASS="caption-text"))
        elif isinstance(node.parent, nodes.container) and node.parent.get(
            "literal_block"
        ):
            self.body.append(self.starttag(node, "span", "", CLASS="caption-text"))
        else:
            self.body.append(self.starttag(node, "p", "", CLASS="caption"))

    def visit_desc(self, node: Element) -> None:
        """Add a class ``code-definition`` to definition lists.

        For code objects, like functions, classes, methods, etc.
        to distinguish them from regular definition lists.
        """
        cl = node["objtype"] + " code-definition"
        self.body.append(self.starttag(node, "dl", CLASS=cl))

    def visit_desc_signature(self, node: Element) -> None:
        """Add the accordion class to the <dt> element.

        This will make the definition list collapsible,
        if the configuration option ``html_collapsible_definitions``
        is set.
        """
        attrs = {
            "data-controller": "collapsible",
            "data-action": "click->collapsible#expandAccordion",
        }
        # only add this, if the following dd is not empty.
        dd = node.next_node(addnodes.desc_content, siblings=True)
        if self.config.html_collapsible_definitions and len(dd.astext()) > 0:
            self.body.append(self.starttag(node, "dt", CLASS="accordion", **attrs))
        else:
            self.body.append(self.starttag(node, "dt"))

        self.protect_literal_text += 1

    def depart_desc_signature(self, node: Element) -> None:
        """Change permalinks for code definitions.

        Functions, methods, command line options, etc.
        "Copy link to this definition"
        """
        dd = node.next_node(addnodes.desc_content, siblings=True)
        if self.config.html_collapsible_definitions and len(dd.astext()) > 0:
            self.body.append(EXPAND_MORE_BUTTON)

        super().depart_desc_signature(node)

    def depart_desc_signature_line(self, node: Element) -> None:
        """Change permalinks for code definitions.

        This method is only relevant for mulitline definitions,
        which I think only happen in C and C++ domains.
        """
        if self.config.html_collapsible_definitions:
            self.body.append(EXPAND_MORE_BUTTON)
        super().depart_desc_signature_line(node)

    def visit_desc_content(self, node: Element) -> None:
        """Add panel class to definitions."""
        if self.config.html_collapsible_definitions and len(node.astext()) > 0:
            self.body.append(self.starttag(node, "dd", CLASS="panel"))
        else:
            self.body.append(self.starttag(node, "dd"))

    def visit_desc_inline(self, node: Element) -> None:
        """Change `span` to `code`."""
        self.body.append(self.starttag(node, "code", ""))

    def depart_desc_inline(self, node: Element) -> None:
        """Change `span` to `code`."""
        self.body.append("</code>")

    def visit_desc_name(self, node: Element) -> None:
        """Change `span` to `code`."""
        self.body.append(self.starttag(node, "code", ""))

    def depart_desc_name(self, node: Element) -> None:
        """Change `span` to `code`."""
        self.body.append("</code>")

    def visit_desc_addname(self, node: Element) -> None:
        """Change `span` to `code`."""
        self.body.append(self.starttag(node, "code", ""))

    def depart_desc_addname(self, node: Element) -> None:
        """Change `span` to `code`."""
        self.body.append("</code>")

    def visit_literal_block(self, node: Element) -> None:
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

            if lang is self.builder.config.highlight_language:
                # only pass highlighter options for original language
                opts = self.builder.config.highlight_options
            else:
                opts = {}

            if linenos and self.builder.config.html_codeblock_linenos_style:
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
                self.body.append('<div class="code-wrapper" data-controller="code">\n')

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

    def depart_literal_block(self, node: Element) -> None:
        """Close literal blocks.

        Provide the closing tag for non-highlighted code blocks.
        This method is skipped with ``raise nodes.SkipNode``
        for highlighted code blocks.
        """
        self.body.append("</code></pre>\n")

    def visit_container(self, node: Element) -> None:
        """Overide for code blocks with captions."""
        if node.get("literal_block"):
            node.html5tagname = "div"
            self.body.append('<div class="code-wrapper" data-controller="code">\n')
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

    def depart_reference(self, node: Element) -> None:
        """Add external link icon."""
        if "refuri" in node and not node.get("internal"):
            self.body.append(ICONS["external_link"])
        super().depart_reference(node)

    def visit_emphasis(self, node: Element) -> None:
        """Change tags for emphasized literals.

        Google recommends using ``<var>`` tags inside ``<code>`` tags
        for placeholders.

        https://developers.google.com/style/placeholders
        """
        if isinstance(node.parent, nodes.literal):
            self.body.append(self.starttag(node, "var", ""))
        else:
            super().visit_emphasis(node)

    def depart_emphasis(self, node: Element) -> None:
        """Change closing tag for emphasized literals."""
        if isinstance(node.parent, nodes.literal):
            self.body.append("</var>")
        else:
            super().depart_emphasis(node)


def setup(app: "Sphinx") -> Dict[str, Any]:
    """Use the AwesomeHTMLTranslator for the html and dirhtml builders.

    This function makes this available as extension.
    """
    app.set_translator("html", AwesomeHTMLTranslator)
    app.set_translator("dirhtml", AwesomeHTMLTranslator)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
