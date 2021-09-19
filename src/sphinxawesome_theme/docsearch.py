"""Add Algolia DocSearch to Sphinx.

This Sphinx extension adds DocSearch to your Sphinx project.

:copyright: Kai Welke.
:license: MIT
"""
import os
from pathlib import Path
from typing import Any, Dict

from docutils.nodes import Node
from dotenv import load_dotenv
from sphinx.application import Sphinx
from sphinx.util import progress_message

from . import __version__


@progress_message("Set up DocSearch")
def setup_docsearch(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: Dict[str, Any],
    doctree: Node,
) -> None:
    """Set up Docsearch.

    Merge the config to the global context.
    This allows replacing of Jinja2 templates
    """
    docsearch_config = {
        "docsearch": app.config.html_awesome_docsearch,
        "docsearch_container": (
            os.getenv("DOCSEARCH_CONTAINER") or app.config.docsearch_container
        ),
        "docsearch_api_key": (
            os.getenv("DOCSEARCH_API_KEY") or app.config.docsearch_api_key
        ),
        "docsearch_index_name": (
            os.getenv("DOCSEARCH_INDEX_NAME") or app.config.docsearch_index_name
        ),
    }
    app.builder.globalcontext.update(docsearch_config)  # type: ignore[union-attr]


def setup(app: Sphinx) -> Dict[str, Any]:
    """Register the extension."""
    app.add_css_file("docsearch.css", priority=150)
    load_dotenv(dotenv_path=(Path(app.confdir) / ".env"))
    app.connect("html-page-context", setup_docsearch)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
