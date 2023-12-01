"""Test the correct handling of deprecated options."""

from io import StringIO

import pytest
from sphinx.application import Sphinx
from sphinxawesome_theme import logos


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinxawesome_theme", "sphinxawesome_theme.deprecated"],
    },
)
def test_handles_deprecated_extension(app: Sphinx, warning: StringIO) -> None:
    """It raises a warning when loading the theme as an extension and sets up the internal extensions."""
    app.build()

    assert (
        'Including `sphinxawesome_theme` in your `extensions` is deprecated. Setting `html_theme = "sphinxawesome_theme"` is enough. You can load the optional `sphinxawesome_theme.highlighting` extension.'
        in warning.getvalue()
    )
    assert "sphinxawesome_theme.highlighting" in app.extensions


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


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinxawesome_theme.deprecated"],
        "html_awesome_docsearch": True,
    },
)
def test_handles_deprecated_docsearch(app: Sphinx, warning: StringIO) -> None:
    """It handles the deprecated `html_awesome_docsearch` option."""
    app.build()

    assert (
        "`html_awesome_docsearch` is deprecated. Use the `sphinx-docsearch` extension instead."
        in warning.getvalue()
    )


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinxawesome_theme.deprecated"],
        "html_collapsible_definitions": True,
    },
)
def test_handles_collapsible_definitions(app: Sphinx, warning: StringIO) -> None:
    """It handles warning about the deprecated `html_collapsible_definitions` option."""
    app.build()

    assert (
        "`html_collapsible_definitions` is deprecated. Use the `sphinx-design` extension instead."
        in warning.getvalue()
    )


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinxawesome_theme.deprecated"],
        "html_awesome_headerlinks": True,
    },
)
def test_handles_awesome_headerlinks(app: Sphinx, warning: StringIO) -> None:
    """It handles the deprecated `html_awesome_headerlinks` option."""
    app.build()

    assert (
        "`html_awesome_headerlinks` is deprecated. Use `html_theme_options = {'awesome_headerlinks: True '} instead."
        in warning.getvalue()
    )
    assert app.config.html_theme_options["awesome_headerlinks"] is True


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinxawesome_theme.deprecated"],
        "html_awesome_external_links": True,
    },
)
def test_handles_awesome_external_links(app: Sphinx, warning: StringIO) -> None:
    """It handles the deprecated `html_awesome_external_links` option."""
    app.build()

    assert (
        "`html_awesome_external_links` is deprecated. Use `html_theme_options = {'awesome_external_links: True '} instead."
        in warning.getvalue()
    )
    assert app.config.html_theme_options["awesome_external_links"] is True


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinxawesome_theme.deprecated"],
        "html_awesome_code_headers": True,
    },
)
def test_handles_awesome_code_headers(app: Sphinx, warning: StringIO) -> None:
    """It handles the deprecated `html_awesome_code_headers` option."""
    app.build()

    # How can I check for the standard output message `logger.info`?
    assert len(warning.getvalue()) == 0
