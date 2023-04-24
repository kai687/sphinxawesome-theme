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
    """Override methods to improve the usability."""

    def visit_reference(self: "AwesomeHTMLTranslator", node: Element) -> None:
        """Override: Add additional attributes to external links.

        Unfortunately, this method isn't easy to extend, so I copy and paste it here.
        """
        atts = {"class": "reference"}
        if node.get("internal") or "refuri" not in node:
            atts["class"] += " internal"
        else:
            atts["class"] += " external"
            atts["rel"] = "nofollow noopener"
        if "refuri" in node:
            atts["href"] = node["refuri"] or "#"
            if self.settings.cloak_email_addresses and atts["href"].startswith(
                "mailto:"
            ):
                atts["href"] = self.cloak_mailto(atts["href"])
                self.in_mailto = True
        else:
            assert (  # noqa
                "refid" in node
            ), 'References must have "refuri" or "refid" attribute.'
            atts["href"] = "#" + node["refid"]
        if not isinstance(node.parent, nodes.TextElement):
            assert len(node) == 1 and isinstance(node[0], nodes.image)  # noqa
            atts["class"] += " image-reference"
        if "reftitle" in node:
            atts["title"] = node["reftitle"]
        if "target" in node:
            atts["target"] = node["target"]
        self.body.append(self.starttag(node, "a", "", **atts))

        if node.get("secnumber"):
            self.body.append(
                ("%s" + self.secnumber_suffix) % ".".join(map(str, node["secnumber"]))
            )

    def depart_reference(self: "AwesomeHTMLTranslator", node: Element) -> None:
        """Add external link icon."""
        if not (node.get("internal") and "refuri" in node):
            self.body.append(ICONS["external_link"])
        super().depart_reference(node)


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
