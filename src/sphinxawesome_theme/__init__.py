"""The Sphinx awesome theme as a Python package.

:copyright: Copyright Kai Welke.
:license: MIT, see LICENSE for details
"""

from __future__ import annotations

from dataclasses import dataclass, field
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any, TypedDict

from sphinx.application import Sphinx
from sphinx.util import logging
from sphinxcontrib.serializinghtml import JSONHTMLBuilder

from . import jinja_functions, jsonimpl, logos, postprocess, toc

logger = logging.getLogger(__name__)

try:
    # obtain version from `pyproject.toml` via `importlib.metadata.version()`
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"


class LinkIcon(TypedDict):
    """A link to an external resource, represented by an icon."""

    link: str
    """The absolute URL to an external resource."""
    icon: str
    """An SVG icon as a string."""


@dataclass
class ThemeOptions:
    """Configuration options for the HTML theme."""

    show_scrolltop: bool = False
    """Show a scroll to top button (Not implemented yet)."""

    show_prev_next: bool = True
    """Show links to previous/next pages."""

    awesome_header_links: bool = True
    """Clicking a headerlink copies the URL to the clipboard."""

    awesome_external_links: bool = False
    """Show an icon after external links."""

    main_nav_links: dict[str, str] = field(default_factory=dict)
    """Navigation links to include in the site header."""

    extra_header_link_icons: dict[str, LinkIcon] = field(default_factory=dict)
    """Extra icons to include on the right side of the header.

    Example:

    extra_header_link_icons: {
        "label": {
            "link": <url>,
            "icon": <svg>,
        }
    }
    """

    logo_light: str | None = None
    """A path to a logo for the light mode.

    If you're using separate logos for light and dark mode,
    you **must** provide both logos.
    """

    logo_dark: str | None = None
    """A path to a logo for the dark mode.

    If you're using separate logos for light and dark mode,
    you **must** provide both logos.
    """


def setup(app: Sphinx) -> dict[str, Any]:
    """Register the theme and its extensions wih Sphinx."""
    here = Path(__file__).parent.resolve()

    app.add_html_theme(name="sphinxawesome_theme", theme_path=str(here))

    # Add the CSS overrides if we're using the `sphinx-design` extension
    if "sphinx_design" in app.extensions:
        app.add_css_file("awesome-sphinx-design.css", priority=900)

    # The theme is set up _after_ extensions are set up,
    # so I can't use internal extensions.
    # For the same reason, I also can't call the `config-inited` event
    app.connect("builder-inited", logos.update_config)
    app.connect("html-page-context", logos.setup_logo_path)
    app.connect("html-page-context", jinja_functions.setup_jinja)
    app.connect("html-page-context", toc.change_toc)
    app.connect("build-finished", logos.copy_logos)
    app.connect("build-finished", postprocess.post_process_html)

    JSONHTMLBuilder.out_suffix = ".json"
    JSONHTMLBuilder.implementation = jsonimpl
    JSONHTMLBuilder.indexer_format = jsonimpl

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
