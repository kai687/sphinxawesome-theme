"""Define custom filters for Jinja2 templates.

:copyright: Copyright, Kai Welke.
:license: MIT, see LICENSE for details.
"""

import json
import posixpath
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


def _get_manifest_json(app: Sphinx) -> Any:
    """Read the ``manifest.json`` file.

    Webpack writes a file ``manifest.json`` in the theme's static directory.
    This file has the mapping between hashed and unhashed filenames.
    Returns a dictionary with this mapping.
    """
    if app.builder and app.builder.theme:  # type: ignore[attr-defined]
        # find the first 'manifest.json' file in the theme's directories
        for entry in app.builder.theme.get_theme_dirs()[::-1]:  # type: ignore[attr-defined] # noqa: E501,B950
            manifest = path.join(entry, "static", "manifest.json")
            if path.isfile(manifest):
                with open(manifest) as m:
                    return json.load(m)
        else:
            return {}
    else:
        return {}


def _make_asset_url(app: Sphinx, asset: str) -> Any:
    """Turn a *clean* asset file name to a hashed one."""
    manifest = _get_manifest_json(app)

    # return the asset itself if it is not in the manifest
    return manifest.get(asset, asset)


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
        # must override `pageurl` for directory builder
        if app.builder.name == "dirhtml":
            context["pageurl"] = posixpath.join(app.config.html_baseurl, pagename + "/")


def setup(app: Sphinx) -> Dict[str, Any]:
    """Register this jinja filter as extension."""
    app.connect("html-page-context", setup_jinja)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
