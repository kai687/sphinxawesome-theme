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
    """Configuration options for the Awesome Theme.

    Sphinx :confval:`sphinx:html_theme_options` is a dictionary,
    which makes it easy to missspell an option or use the wrong type.

    Use the ``ThemeOptions`` class to make sure, you're using the correct options.

    In your Sphinx configuration, add the following import at the top:

    .. code-block:: python
       :caption: File: conf.py

       from dataclass import asdict
       from sphinxawesome_theme import ThemeOptions

    Then, use the following code to set up the ``html_theme_options``:

    .. code-block:: python
       :caption: File: conf.py

       theme_options = ThemeOptions(
           # Add the options.
       )

       html_theme_options = asdict(theme_options)
    """

    show_prev_next: bool = True
    """Controls whether to show links to the previous and next pages in the hierarchy."""

    show_breadcrumbs: bool = True
    """Controls whether to include `breadcrumbs <https://en.wikipedia.org/wiki/Breadcrumb_navigation>`_ links at the top of each page."""

    breadcrumbs_separator: str = "/"
    """The separator for the breadcrumbs links."""

    awesome_header_links: bool = True
    """Controls whether clicking a headerlink should copy the URL to the clipboard."""

    show_scrolltop: bool = False
    """Controls whether to show a button that scrolls to the top of the page when clicked."""

    awesome_external_links: bool = False
    """Show icons after external links."""

    main_nav_links: dict[str, str] = field(default_factory=dict)
    """A dict with links to include in the site header."""

    extra_header_link_icons: dict[str, LinkIcon] = field(default_factory=dict)
    """A dict with extra icons to include on the right of the search bar."""

    logo_light: str | None = None
    """A path to a logo for the light mode. If you're using separate logos for light and dark mode, you **must** provide both logos."""

    logo_dark: str | None = None
    """A path to a logo for the dark mode. If you're using separate logos for light and dark mode, you **must** provide both logos."""


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
