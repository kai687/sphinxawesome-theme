"""The Sphinx awesome theme as a Python package.

:copyright: Copyright Kai Welke.
:license: MIT, see LICENSE_ for details

.. _LICENSE: https://github.com/kai687/sphinxawesome-theme/blob/master/LICENSE
"""

from __future__ import annotations

from dataclasses import dataclass, field
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any, TypedDict

from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util import logging
from sphinxcontrib.serializinghtml import JSONHTMLBuilder

from . import jsonimpl, logos

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


def post_config_setup(app: Sphinx, config: Config) -> None:
    """Set up extensions if configuration is ready."""
    if config.html_awesome_highlighting:
        app.setup_extension("sphinxawesome_theme.highlighting")

    # The awesome code headers are handled in `postprocessing`
    if config.html_awesome_postprocessing or config.html_awesome_code_headers:
        app.setup_extension("sphinxawesome_theme.postprocess")

    # Add the CSS overrides if we're using the `sphinx-design` extension
    if "sphinx_design" in app.extensions:
        app.add_css_file("awesome-sphinx-design.css", priority=900)


def setup(app: Sphinx) -> dict[str, Any]:
    """Register the theme and its extensions wih Sphinx."""
    here = Path(__file__).parent.resolve()

    app.add_html_theme(name="sphinxawesome_theme", theme_path=str(here))

    # TODO: Adding these options require the theme being loaded as an extension
    #       Try converting this into `theme_options`
    app.add_config_value(
        name="html_awesome_postprocessing", default=True, rebuild="html", types=(bool)
    )

    app.add_config_value(
        name="html_awesome_highlighting", default=True, rebuild="html", types=(bool)
    )

    # TODO: Not implemented yet in the new version
    app.add_config_value(
        name="html_awesome_code_headers", default=True, rebuild="html", types=(str)
    )

    app.setup_extension("sphinxawesome_theme.jinja_functions")
    app.setup_extension("sphinxawesome_theme.toc")

    app.connect("config-inited", post_config_setup)
    app.connect("builder-inited", logos.update_config)
    app.connect("html-page-context", logos.setup_logo_path)
    app.connect("build-finished", logos.copy_logos)

    JSONHTMLBuilder.out_suffix = ".json"
    JSONHTMLBuilder.implementation = jsonimpl
    JSONHTMLBuilder.indexer_format = jsonimpl

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
