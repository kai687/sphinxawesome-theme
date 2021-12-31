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
    """Set up DocSearch.

    Config can be provided via environment variables, a `.env.` file,
    or the Sphinx configuration file.
    """
    # load `.env` file into environment
    load_dotenv(dotenv_path=(Path(app.confdir) / ".env"))

    docsearch_config = {
        "container": (
            os.getenv("DOCSEARCH_CONTAINER")
            or app.config.docsearch_config.get("container", "#docsearch")
        ),
        "app_id": (
            os.getenv("DOCSEARCH_APP_ID") or app.config.docsearch_config.get("app_id")
        ),
        "api_key": (
            os.getenv("DOCSEARCH_API_KEY") or app.config.docsearch_config.get("api_key")
        ),
        "index_name": (
            os.getenv("DOCSEARCH_INDEX_NAME")
            or app.config.docsearch_config.get("index_name")
        ),
    }

    # if we want to use `docsearch` we don't need any other JS file from Sphinx
    if app.config.html_awesome_docsearch:
        context["script_files"] = []

    context["docsearch"] = app.config.html_awesome_docsearch
    # update local context for rendering the `layout.html` templates for every page
    context["docsearch_config"] = docsearch_config
    # update the global context for writing the `docsearch_config.js` file
    app.builder.globalcontext["docsearch_config"] = docsearch_config  # type: ignore [union-attr] # noqa: B950,E501


def setup(app: Sphinx) -> Dict[str, Any]:
    """Register the extension."""
    app.add_css_file("docsearch.css", priority=150)
    app.connect("html-page-context", setup_docsearch)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
