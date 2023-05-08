"""The Sphinx awesome theme as a Python package.

:copyright: Copyright Kai Welke.
:license: MIT, see LICENSE_ for details

.. _LICENSE: https://github.com/kai687/sphinxawesome-theme/blob/master/LICENSE
"""

from __future__ import annotations

from dataclasses import dataclass, field
from importlib.metadata import PackageNotFoundError, version
from os import path
from pathlib import Path
from typing import Any, TypedDict

from docutils.nodes import Node
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util import isurl, logging
from sphinx.util.fileutil import copy_asset_file
from sphinxcontrib.serializinghtml import JSONHTMLBuilder

from . import jsonimpl

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


def get_theme_options(app: Sphinx) -> dict[str, Any]:
    """Return theme options for the application.

    Adapted from the ``pydata_sphinx_theme``.
    https://github.com/pydata/pydata-sphinx-theme/blob/f15ecfed59a2a5096c05496a3d817fef4ef9a0af/src/pydata_sphinx_theme/utils.py
    """
    if hasattr(app.builder, "theme_options"):
        return app.builder.theme_options
    elif hasattr(app.config, "html_theme_options"):
        return app.config.html_theme_options
    else:
        return {}


def update_config(app: Sphinx) -> None:
    """Update the configuration, handling the ``builder-inited`` event.

    Adapted from the ``pydata_sphinx_theme``:
    https://github.com/pydata/pydata-sphinx-theme/blob/f15ecfed59a2a5096c05496a3d817fef4ef9a0af/src/pydata_sphinx_theme/__init__.py
    """
    theme_options = get_theme_options(app)

    # Check logo config
    dark_logo = theme_options.get("logo_dark")
    light_logo = theme_options.get("logo_light")
    if app.config.html_logo and (dark_logo or light_logo):
        # For the rendering of the logos, see ``header.html`` and ``sidebar.html``
        logger.warning(
            "Conflicting theme options: use either `html_logo` or `logo_light` and `logo_dark`)."
        )
    if not (dark_logo and light_logo):
        logger.warning("You must use `logo_light` and `logo_dark` together.")


def setup_logo_path(
    app: Sphinx, pagename: str, templatename: str, context: dict, doctree: Node
) -> None:
    """Update the logo path for the templates."""
    theme_options = get_theme_options(app)
    for kind in ["dark", "light"]:
        logo = theme_options.get(f"logo_{kind}")
        if logo and not isurl(logo):
            context[f"theme_logo_{kind}"] = path.basename(logo)


def copy_logos(app: Sphinx, exc: Exception | None) -> None:
    """Copy the light and dark logos."""
    theme_options = get_theme_options(app)
    static_dir = str(Path(app.builder.outdir) / "_static")

    for kind in ["dark", "light"]:
        logo = theme_options.get(f"logo_{kind}")
        if logo and not isurl(logo):
            logo_path = Path(app.builder.confdir) / logo
            if not logo_path.exists():
                logger.warning("Path to logo %s does not exist.", logo)
            copy_asset_file(str(logo_path), static_dir)


def post_config_setup(app: Sphinx, config: Config) -> None:
    """Set up extensions if configuration is ready."""
    if config.html_awesome_highlighting:
        app.setup_extension("sphinxawesome_theme.highlighting")

    if config.html_awesome_external_links:
        app.setup_extension("sphinxawesome_theme.html_translator")

    # The awesome code headers are handled in `postprocessing`
    if config.html_awesome_postprocessing or config.html_awesome_code_headers:
        app.setup_extension("sphinxawesome_theme.postprocess")

    if config.html_awesome_docsearch:
        app.setup_extension("sphinxawesome_theme.docsearch")

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

    app.add_config_value(
        name="html_awesome_external_links", default=False, rebuild="html", types=(bool)
    )

    app.add_config_value(
        name="html_awesome_docsearch", default=False, rebuild="html", types=(bool)
    )

    app.add_config_value(
        name="docsearch_config", default={}, rebuild="html", types=(dict)
    )

    app.add_config_value(
        name="html_awesome_headerlinks", default=True, rebuild="html", types=(str)
    )

    # TODO: Not implemented yet in the new version
    app.add_config_value(
        name="html_awesome_code_headers", default=True, rebuild="html", types=(str)
    )

    app.setup_extension("sphinxawesome_theme.jinja_functions")
    app.setup_extension("sphinxawesome_theme.toc")
    app.connect("config-inited", post_config_setup)
    app.connect("builder-inited", update_config)
    app.connect("html-page-context", setup_logo_path)
    app.connect("build-finished", copy_logos)

    JSONHTMLBuilder.out_suffix = ".json"
    JSONHTMLBuilder.implementation = jsonimpl
    JSONHTMLBuilder.indexer_format = jsonimpl

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
