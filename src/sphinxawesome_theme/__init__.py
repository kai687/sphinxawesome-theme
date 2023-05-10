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
    """Helper class for configuring the Awesome Theme.

    Each attribute becomes a key in the :confval:`sphinx:html_theme_options` dictionary.
    """

    show_prev_next: bool = True
    """If ``True``, the theme includes links to the previous and next pages in the hierarchy."""

    show_breadcrumbs: bool = True
    """If ``True``, the theme includes `breadcrumbs <https://en.wikipedia.org/wiki/Breadcrumb_navigation>`_ links on every page except the root page."""

    breadcrumbs_separator: str = "/"
    """The separator for the breadcrumbs links."""

    awesome_header_links: bool = True
    """If ``True``, clicking a headerlink copies its URL to the clipboard."""

    show_scrolltop: bool = False
    """If ``True``, the theme shows a button that scrolls to the top of the page when clicked."""

    awesome_external_links: bool = False
    """If ``True``, the theme includes an icon after external links and adds ``rel="nofollow noopener"`` to the links' attributes."""

    main_nav_links: dict[str, str] = field(default_factory=dict)
    """A dictionary with links to include in the site header.

    The keys of this dictionary are the labels for the links.
    The values are absolute or relative URLs.
    """

    extra_header_link_icons: dict[str, LinkIcon] = field(default_factory=dict)
    """A dictionary with extra icons to include on the right of the search bar.

    The keys are labels for the link's ``title`` attribute.
    The values are themselves :class:`LinkIcon`.
    """

    logo_light: str | None = None
    """A path to a logo for the light mode. If you're using separate logos for light and dark mode, you **must** provide both logos."""

    logo_dark: str | None = None
    """A path to a logo for the dark mode. If you're using separate logos for light and dark mode, you **must** provide both logos."""

    globaltoc_includehidden: bool = True
    """If ``True``, the theme includes entries from *hidden*
    :sphinxdocs:`toctree <usage/restructuredtext/directives.html#directive-toctree>` directives in the sidebar.

    The ``toctree`` directive generates a list of links on the page where you include it,
    unless you set the ``:hidden:`` option.
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
