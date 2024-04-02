"""Define custom filters for Jinja2 templates.

:copyright: Copyright, Kai Welke.
:license: MIT, see LICENSE for details.
"""

from __future__ import annotations

import posixpath
from typing import Any

from docutils.nodes import Node
from sphinx.application import Sphinx


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
    context: dict[str, Any],
    doctree: Node,
) -> None:
    """Register a function as a Jinja2 filter."""
    # must override `pageurl` for directory builder
    if app.builder.name == "dirhtml" and app.config.html_baseurl:
        context["pageurl"] = _make_canonical(app, pagename)
