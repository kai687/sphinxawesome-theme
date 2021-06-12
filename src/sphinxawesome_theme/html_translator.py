"""Modification of the Sphinx HTML5 translator.

Overwrite several methods to improve the HTML output.

Improve headerlinks
   Instead of writing "permalink to this headline", we write
   "Copy link to section: <SECTIONNAME>" and display an icon
   instead of the '¶' character.

Remove unnecessary nesting

:copyright: Copyright Kai Welke.
:license: MIT, see LICENSE for details.
"""
from typing import Any, Dict

from docutils import nodes
from docutils.nodes import Element
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.locale import _
from sphinx.util import logging
from sphinx.writers.html5 import HTML5Translator

from . import __version__
from .icons import ICONS

logger = logging.getLogger(__name__)

COPY_BUTTON = (
    "<button class='copy tooltipped tooltipped-nw' aria-label='Copy this code'>"
    + ICONS["copy"]
    + "</button>\n"
)

EXPAND_MORE_BUTTON = (
    "<button class='expand-more tooltipped tooltipped-nw' "
    "aria-label='Expand this section' aria-expanded='false'>"
    + ICONS["expand_more"]
    + "</button>"
)


class AwesomeHTMLTranslator(HTML5Translator):
    """Override a few methods to improve the usability."""

    def depart_title(self, node: Element) -> None:
        """Change the permalinks for headlines.

        - for headlines: "Copy link to section: <section title>"
        - for tables: "Copy link to this table"
        - for admonitions: "Copy link to this <type>"

        Admonitions don't have an ID by default.
        The AdmonitionID post-transform adds
        IDs to admonitions.
        """
        close_tag = self.context[-1]
        if (
            self.config.html_permalinks
            and self.builder.add_permalinks
            and node.parent.hasattr("ids")
            and node.parent["ids"]
        ):
            # add permalink anchor to normal headings
            if close_tag.startswith("</h"):
                self.add_permalink_ref(
                    node.parent, _(f"Copy link to section: {node.astext()}.")
                )
            # and to headings when the 'contents' directive is used
            elif close_tag.startswith("</a></h"):
                self.body.append(
                    "</a><a role='button' "
                    "class='headerlink tooltipped tooltipped-ne' "
                    'href="#{}" '
                    'aria-label="Copy link to this section: {}">'.format(
                        node.parent["ids"][0], node.astext()
                    )
                    + ICONS["headerlink"]
                )
            elif isinstance(node.parent, nodes.table):
                self.body.append("</span>")
                self.add_permalink_ref(node.parent, _("Copy link to this table."))
            elif isinstance(node.parent, nodes.Admonition):
                admon_type = type(node.parent).__name__
                self.add_permalink_ref(
                    node.parent, _(f"Copy link to this {admon_type}.")
                )
        elif isinstance(node.parent, nodes.table):
            self.body.append("</span>")

        self.body.append(self.context.pop())
        if self.in_document_title:  # type: ignore
            self.title = self.body[self.in_document_title : -1]  # type: ignore
            self.in_document_title = 0
            self.body_pre_docinfo.extend(self.body)
            self.html_title.extend(self.body)
            del self.body[:]

    def add_permalink_ref(self, node: Element, title: str) -> None:
        """Add an icon instead of the ¶ symbol.

        Note that user-defined permalink characters specified via
        `html_add_permalinks` are ignored.

        Since clicking the permalink icon copies the link to the clipboard,
        this should be a button element, but there is some magic with the
        resolution of `href` attributes happening in Sphinx.
        """
        if node["ids"] and self.builder.add_permalinks and self.config.html_permalinks:
            headerlink = (
                '<a role="button" class="headerlink tooltipped tooltipped-ne" '
                'href="#{}" aria-label="{}">'.format(node["ids"][0], title)
            )
            headerlink += ICONS["headerlink"] + "</a>"
            self.body.append(headerlink)

    def visit_caption(self, node: Element) -> None:
        """Use semantic elements."""
        if isinstance(node.parent, nodes.figure):
            self.body.append("<figcaption>")
            self.add_fignumber(node.parent)
            self.body.append(self.starttag(node, "span", "", CLASS="caption-text"))
        elif isinstance(node.parent, nodes.container) and node.parent.get(
            "literal_block"
        ):
            self.body.append(self.starttag(node, "span", ""))
            self.body.append(self.starttag(node, "span", "", CLASS="caption-text"))
        else:
            self.body.append(self.starttag(node, "p", "", CLASS="caption"))

    def depart_caption(self, node: Element) -> None:
        """Change the permalinks for captions.

        - for code blocks: Copy link to this code block
        - for images: Copy link to this image
        - for table of contents: Copy link to this table of contents.
        """
        self.body.append("</span>")

        # append permalink if available
        if isinstance(node.parent, nodes.container) and node.parent.get(
            "literal_block"
        ):
            self.add_permalink_ref(node.parent, _("Copy link to this code block."))
            self.body.append("</span>")
        if isinstance(node.parent, nodes.figure):
            self.add_permalink_ref(node.parent, _("Copy link to this image."))
        elif node.parent.get("toctree"):
            self.add_permalink_ref(
                node.parent.parent, _("Copy link to this table of contents.")
            )

        if isinstance(node.parent, nodes.container) and node.parent.get(
            "literal_block"
        ):
            self.body.append(COPY_BUTTON)
            self.body.append("</div>\n")
        else:
            self.body.append("</p>\n")

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
        # only add this, if the following dd is not empty.
        dd = node.next_node(addnodes.desc_content, siblings=True)
        if self.config.html_collapsible_definitions and len(dd.astext()) > 0:
            self.body.append(self.starttag(node, "dt", CLASS="accordion"))
        else:
            self.body.append(self.starttag(node, "dt"))

        self.protect_literal_text += 1

    def depart_desc_signature(self, node: Element) -> None:
        """Change permalinks for code definitions.

        Functions, methods, command line options, etc.
        "Copy link to this definition"
        """
        self.protect_literal_text -= 1

        if not node.get("is_multiline"):
            self.add_permalink_ref(node, _("Copy link to this definition."))
        dd = node.next_node(addnodes.desc_content, siblings=True)
        if self.config.html_collapsible_definitions and len(dd.astext()) > 0:
            self.body.append(EXPAND_MORE_BUTTON)
        self.body.append("</dt>\n")

    def depart_desc_signature_line(self, node: Element) -> None:
        """Change permalinks for code definitions.

        This method is only relevant for mulitline definitions,
        which I think only happen in C and C++ domains.
        """
        if node.get("add_permalink"):
            self.add_permalink_ref(node.parent, _("Copy link to this definition."))
        if self.config.html_collapsible_definitions:
            self.body.append(EXPAND_MORE_BUTTON)
        self.body.append("<br />")

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

        All code blocks have a header with at least a copy button.
        For code blocks with syntax highlighting, the language is
        shown on the left side and an optional caption is included
        in the center.
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

            # Code blocks that don't have a caption are not wrapped inside a <container>
            # node so we add the header here. With captions, see: visit_caption
            if not (
                isinstance(node.parent, nodes.container)
                and node.parent.get("literal_block")
            ):

                self.body.append(self.starttag(node, "div", CLASS="highlight"))

                code_header = "<div class='code-header'>\n"
                code_lang = lang.replace("default", "python").replace(
                    "console", "shell"
                )
                code_header += f"<span class='code-lang'>{code_lang}</span>\n"
                code_header += COPY_BUTTON
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
            self.body.append(self.starttag(node, "div", CLASS="highlight"))
            code_header = "<div class='code-header'>\n"
            code_header += COPY_BUTTON
            code_header += "</div>\n"
            self.body.append(code_header)
            self.body.append("<pre><code>")

    def depart_literal_block(self, node: Element) -> None:
        """Close literal blocks.

        We need to provide the closing tag for non-highlighted
        code blocks. This method is skipped (``raise nodes.SkipNode``)
        for highlighted code blocks.
        """
        self.body.append("</code></pre>\n")
        self.body.append("</div>\n")

    def visit_container(self, node: Element) -> None:
        """Overide for code blocks with captions."""
        if node.get("literal_block"):
            # for docutils >0.17
            node.html5tagname = "div"
            self.body.append(self.starttag(node, "div", CLASS="highlight"))
            lang = node.get("language")
            code_header = "<div class='code-header'>\n"
            code_header += (
                f"<span class='code-lang'>{lang.replace('default', 'python')}</span>\n"
            )
            self.body.append(code_header)
        else:
            super().visit_container(node)

    def depart_reference(self, node: Element) -> None:
        """Add external link icon."""
        if "refuri" in node and not node.get("internal"):
            self.body.append(ICONS["external_link"])
        super().depart_reference(node)


def setup(app: "Sphinx") -> Dict[str, Any]:
    """Use the AwesomeHTMLTranslator for the html and dirhtml builders.

    This function makes this available as extension.
    """
    app.set_translator("html", AwesomeHTMLTranslator)
    app.set_translator("dirhtml", AwesomeHTMLTranslator)
    app.add_config_value("html_collapsible_definitions", False, "html")

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
