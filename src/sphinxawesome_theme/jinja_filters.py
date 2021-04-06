"""Define custom filters for Jinja2 templates.

:copyright: Copyright, Kai Welke.
:license: MIT, see LICENSE for details.
"""
from typing import Any, Dict

from docutils.nodes import Node, make_id
from sphinx.application import Sphinx

from . import __version__


def _make_id_from_title(title: str) -> str:
    """Use the ``docutils.nodes.make_id`` function to create an ID from a title.

    This can be used for creating link targets from headlines.
    E.g. transform "Code, Figures, and Tables" into "code-figures-and-tables",
    which can then be used like this:
    ``<a href=#{{ title|sanitize }}>{{ title }}</a>``
    """
    return make_id(title)


def setup_jinja_filter(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: Dict[str, Any],
    doctree: Node,
) -> None:
    """Register a function as a Jinja2 filter."""
    app.builder.templates.environment.filters["sanitize"] = _make_id_from_title


def setup(app: Sphinx) -> Dict[str, Any]:
    """Register this jinja filter as extension."""
    app.connect("html-page-context", setup_jinja_filter)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
