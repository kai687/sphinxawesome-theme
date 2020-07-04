"""Modification of the Sphinx HTML5 translator with better handling of permalinks.

Instead of "permalink to this headline",
this returns "Copy link to section: *sectionname*".
Clicking on the permalink anchor will copy the link to the clipboard.
This is implemented in JavaScript.

:copyright: Copyright 2020, Kai Welke.
:license: MIT, see LICENSE for details.
"""

from docutils import nodes
from docutils.nodes import Element
from sphinx.locale import _
from sphinx.util import logging
from sphinx.writers.html5 import HTML5Translator

logger = logging.getLogger(__name__)


class BetterHTMLTranslator(HTML5Translator):
    """Override a few methods to produce better permalinks."""

    def depart_title(self, node: Element) -> None:
        """Override permalink addition to headlines."""
        close_tag = self.context[-1]
        if (
            self.permalink_text
            and self.builder.add_permalinks
            and node.parent.hasattr("ids")
            and node.parent["ids"]
        ):
            # add permalink anchor
            if close_tag.startswith("</h"):
                self.add_permalink_ref(
                    node.parent, _(f"Copy link to section: {node.astext()}.")
                )
            elif close_tag.startswith("</a></h"):
                self.body.append(
                    f'</a><a class="headerlink" href="#{node.parent["ids"][0]}" '
                    f'title="{_("Copy link to section: {node.astext()}.")}">'
                    f"{self.permalink_text}"
                )
            elif isinstance(node.parent, nodes.table):
                self.body.append("</span>")
                self.add_permalink_ref(node.parent, _("Copy link to this table"))
            elif isinstance(node.parent, nodes.Admonition):
                self.add_permalink_ref(node.parent, _("Copy link to this admonition."))
                #  self.body.append(
                #  f'<a class="headerlink" href="#{node.parent["ids"][0]}" '
                #  f'title="{_("Copy link to this admonition")}">{self.permalink_text}'
                #  )
        elif isinstance(node.parent, nodes.table):
            self.body.append("</span>")

        self.body.append(self.context.pop())
        if self.in_document_title:
            self.title = self.body[self.in_document_title : -1]
            self.in_document_title = 0
            self.body_pre_docinfo.extend(self.body)
            self.html_title.extend(self.body)
            del self.body[:]

    def depart_caption(self, node: Element) -> None:
        """Override permalink stuff."""
        self.body.append("</span>")

        # append permalink if available
        if isinstance(node.parent, nodes.container) and node.parent.get(
            "literal_block"
        ):
            self.add_permalink_ref(node.parent, _("Copy link to this code block."))
        elif isinstance(node.parent, nodes.figure):
            self.add_permalink_ref(node.parent, _("Copy link to this image."))
        elif node.parent.get("toctree"):
            self.add_permalink_ref(
                node.parent.parent, _("Copy link to this table of contents")
            )

        if isinstance(node.parent, nodes.container) and node.parent.get(
            "literal_block"
        ):
            self.body.append("</div>\n")
        else:
            self.body.append("</p>\n")
