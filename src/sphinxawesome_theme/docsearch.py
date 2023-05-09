"""Add Algolia DocSearch to Sphinx.

This extension replaces the built-in search in Sphinx with Algolia DocSearch.
To load this extension, add:

.. code-block:: python
   :caption: File: conf.py

   extensions += ["sphinxawesome_theme.docsearch"]

:copyright: Kai Welke.
:license: MIT, see LICENSE for details
"""
from __future__ import annotations

from typing import Any

from docutils.nodes import Node
from sphinx.application import Sphinx
from sphinx.builders.dirhtml import DirectoryHTMLBuilder
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.config import Config
from sphinx.locale import __
from sphinx.util import logging
from sphinx.util.display import progress_message

from . import __version__

logger = logging.getLogger(__name__)


@progress_message("DocSearch: check config")
def check_config(app: Sphinx, config: Config) -> None:
    """Set up Algolia DocSearch.

    Log warnings if any of these configuration options are missing:

    - ``docsearch_app_id``
    - ``docsearch_api_key``
    - ``docsearch_index_name``
    """
    if not config.docsearch_app_id:
        logger.warning(
            __("You must provide your Algolia application ID for DocSearch to work.")
        )
    if not config.docsearch_api_key:
        logger.warning(
            __("You must provide your Algolia search API key for DocSearch to work.")
        )
    if not config.docsearch_index_name:
        logger.warning(
            __("You must provide your Algolia index name for DocSearch to work.")
        )


@progress_message("DocSearch: add assets")
def add_docsearch_assets(app: Sphinx, config: Config) -> None:
    """Add the docsearch.css file for DocSearch."""
    app.add_css_file("docsearch.css", priority=150)
    # TODO: add_js_file (currently in `layout.html` I think)


def update_global_context(app: Sphinx, doctree: Node, docname: str) -> None:
    """Update global context with DocSearch configuration."""
    if hasattr(app.builder, "globalcontext"):
        app.builder.globalcontext["docsearch"] = True
        app.builder.globalcontext["docsearch_app_id"] = app.config.docsearch_app_id
        app.builder.globalcontext["docsearch_api_key"] = app.config.docsearch_api_key
        app.builder.globalcontext[
            "docsearch_index_name"
        ] = app.config.docsearch_index_name
        app.builder.globalcontext[
            "docsearch_container"
        ] = app.config.docsearch_container
        app.builder.globalcontext[
            "docsearch_initial_query"
        ] = app.config.docsearch_initial_query
        app.builder.globalcontext[
            "docsearch_placeholder"
        ] = app.config.docsearch_placeholder
        app.builder.globalcontext[
            "docsearch_search_parameter"
        ] = app.config.docsearch_search_parameter
        app.builder.globalcontext[
            "docsearch_missing_results_url"
        ] = app.config.docsearch_missing_results_url


def remove_script_files(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: Node,
) -> None:
    """Remove Sphinx JavaScript files when using DocSearch."""
    context["script_files"].remove("_static/documentation_options.js")
    context["script_files"].remove("_static/doctools.js")
    context["script_files"].remove("_static/sphinx_highlight.js")


def setup(app: Sphinx) -> dict[str, Any]:
    """Register the extension."""
    app.add_config_value("docsearch_app_id", default="", rebuild="html", types=(str))
    app.add_config_value("docsearch_api_key", default="", rebuild="html", types=(str))
    app.add_config_value(
        "docsearch_index_name", default="", rebuild="html", types=(str)
    )
    app.add_config_value(
        "docsearch_container", default="#docsearch", rebuild="html", types=(str)
    )
    app.add_config_value(
        "docsearch_initial_query", default="", rebuild="html", types=(str)
    )
    app.add_config_value(
        "docsearch_placeholder", default="", rebuild="html", types=(str)
    )
    app.add_config_value(
        "docsearch_search_parameter", default="", rebuild="html", types=(str)
    )
    app.add_config_value(
        "docsearch_missing_results_url", default="", rebuild="html", types=(str)
    )

    app.connect("config-inited", check_config)
    app.connect("config-inited", add_docsearch_assets)
    app.connect("doctree-resolved", update_global_context)
    app.connect("html-page-context", remove_script_files)

    # Disable built-in search
    StandaloneHTMLBuilder.search = False
    DirectoryHTMLBuilder.search = False

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
