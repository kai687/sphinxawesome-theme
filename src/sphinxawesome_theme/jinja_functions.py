"""Define custom filters for Jinja2 templates.

:copyright: Copyright, Kai Welke.
:license: MIT, see LICENSE for details.
"""

import json
import posixpath
from functools import partial
from os import path
from typing import Any, Dict

from docutils.nodes import Node
from sphinx.application import Sphinx

from . import __version__


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


def _make_asset_url(app: Sphinx, asset: str) -> Any:
    """Turn a *clean* asset file name to a hashed one."""
    manifest = _get_manifest_json(app)

    # return the asset itself if it is not in the manifest
    return manifest.get(asset, asset)


def _make_canonical(app: Sphinx, pagename: str) -> str:
    """Turn a filepath into the correct canonical link.

    Upstream Sphinx builds the wrong canonical links for the ``dirhtml`` builder.
    """
    canonical = posixpath.join(app.config.html_baseurl, pagename.replace("index", ""))
    if not canonical.endswith("/"):
        canonical += "/"
    return canonical


def setup_jinja(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: Dict[str, Any],
    doctree: Node,
) -> None:
    """Register a function as a Jinja2 filter."""
    if app.builder is not None:
        context["asset"] = partial(_make_asset_url, app)
        # must override `pageurl` for directory builder
        if app.builder.name == "dirhtml" and app.config.html_baseurl:
            context["pageurl"] = _make_canonical(app, pagename)


def setup(app: Sphinx) -> Dict[str, Any]:
    """Register this jinja filter as extension."""
    app.connect("html-page-context", setup_jinja)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
