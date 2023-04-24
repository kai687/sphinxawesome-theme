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
# import re
from typing import Any, Dict

from docutils.nodes import Element
from sphinx.application import Sphinx
from sphinx.util import logging
from sphinx.writers.html5 import HTML5Translator

from . import __version__
from .icons import ICONS

logger = logging.getLogger(__name__)


class AwesomeHTMLTranslator(HTML5Translator):
    """Override a few methods to improve the usability."""

    def depart_reference(self: "AwesomeHTMLTranslator", node: Element) -> None:
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

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
