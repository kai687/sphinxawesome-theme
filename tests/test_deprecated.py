"""Test the correct handling of deprecated options."""

from io import StringIO

import pytest
from sphinx.application import Sphinx
from sphinxawesome_theme import logos


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinxawesome_theme"],
    },
)
def test_handles_deprecated_extension(app: Sphinx, warning: StringIO) -> None:
    """It raises a warning when loading the theme as an extension and sets up the internal extensions."""
    app.build()

    assert (
        'Including `sphinxawesome_theme` in your `extensions` is deprecated. Setting `html_theme = "sphinxawesome_theme"` is enough. You can load the optional `sphinxawesome_theme.docsearch` and `sphinxawesome_theme.highlighting` extensions.'
        in warning.getvalue()
    )
    assert "sphinxawesome_theme.highlighting" in app.extensions
    assert "sphinxawesome_theme.docsearch" in app.extensions


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "html_theme_options": {"nav_include_hidden": True},
    },
)
def test_handles_deprecated_include_hidden(app: Sphinx, warning: StringIO) -> None:
    """It handles the deprecated `nav_include_hidden` option."""
    app.build()
    theme_options = logos.get_theme_options(app)

    assert (
        "Setting `nav_include_hidden` in `html_theme_options` is deprecated. Use `globaltoc_includehidden` in `html_theme_options` instead."
        in warning.getvalue()
    )
    assert "nav_include_hidden" not in theme_options
    assert "globaltoc_includehidden" in theme_options


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "html_theme_options": {"show_nav": False},
    },
)
def test_handles_deprecated_show_nav(app: Sphinx, warning: StringIO) -> None:
    """It handles the deprecated `show_nav` option."""
    app.build()

    theme_options = logos.get_theme_options(app)
    assert (
        "Toggling the sidebar with `show_nav` in `html_theme_options` is deprecated. Control the sidebar with the `html_sidebars` configuration option instead."
        in warning.getvalue()
    )
    assert "show_nav" not in theme_options
    assert app.builder.config.html_sidebars == {"**": []}


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "html_theme_options": {
            "extra_header_links": {
                "link": "link",
                "text": "text",
                "with_icon": {"link": "link", "icon": "icon"},
            }
        },
    },
)
def test_handles_deprecated_extra_header_links(app: Sphinx, warning: StringIO) -> None:
    """It handles the deprecated `extra_header_links` option."""
    app.build()

    theme_options = logos.get_theme_options(app)
    assert (
        "`extra_header_links` is deprecated. Use `main_nav_links` for text links (left side) and `extra_header_link_icons` for icon links (right side) instead."
        in warning.getvalue()
    )
    assert "extra_header_links" not in theme_options
    assert theme_options["main_nav_links"] == {"link": "link", "text": "text"}
    assert theme_options["extra_header_link_icons"] == {
        "with_icon": {"link": "link", "icon": "icon"}
    }
