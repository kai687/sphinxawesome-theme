"""Define custom filters for Jinja2 templates.

:copyright: Copyright, Kai Welke.
:license: MIT, see LICENSE for details.
"""

import json
from functools import partial
from os import path
from typing import Any, Dict

from docutils.nodes import Node, make_id
from sphinx.application import Sphinx

from . import __version__


def _make_id_from_title(title: str) -> Any:
    """Use the ``docutils.nodes.make_id`` function to create an ID from a title.

    This can be used for creating link targets from headlines.
    E.g. transform "Code, Figures, and Tables" into "code-figures-and-tables",
    which can then be used like this:
    ``<a href=#{{ title|sanitize }}>{{ title }}</a>``

    Note: `docutils.nodes.make_id` returns Any. Setting the return type to `str`
    here results in a mypy error in strict mode because of that.
    """
    return make_id(title)


def _make_asset_url(app: Sphinx, asset: str) -> str:
    """Turn a *clean* asset file name to a hashed one.

    Webpack writes a file ``manifest.json`` that has the mapping
    between unhashed and hashed filenames.
    """
    manifest = path.join(app.outdir, "_static", "manifest.json")
    with open(manifest) as m:
        hashed_filenames = json.load(m)

    # return the asset itself if it is not in the manifest
    return hashed_filenames.get(asset, asset)


def setup_jinja(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: Dict[str, Any],
    doctree: Node,
) -> None:
    """Register a function as a Jinja2 filter."""
    if app.builder is not None:
        app.builder.templates.environment.filters["sanitize"] = _make_id_from_title
        context["asset"] = partial(_make_asset_url, app)


def setup(app: Sphinx) -> Dict[str, Any]:
    """Register this jinja filter as extension."""
    app.connect("html-page-context", setup_jinja)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
