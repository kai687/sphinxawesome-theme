"""Unit tests for the sphinxawesome_theme python extensions."""
import pytest
from sphinx.application import Sphinx

import sphinxawesome_theme


def test_returns_version() -> None:
    """It has the correct version."""
    assert sphinxawesome_theme.__version__ == "3.3.0"


@pytest.mark.sphinx("html")
def test_can_compile_default_test(app: Sphinx) -> None:
    """It can compile a basic test and doesn't load any extensions by default."""
    app.build()
    assert app.config.html_theme == "alabaster"
    assert "sphinxawesome_theme" not in app.extensions
    assert "sphinxawesome_theme.html_translator" not in app.extensions
    assert "sphinxawesome_theme.jinja_functions" not in app.extensions
    assert "sphinxawesome_theme.postprocess" not in app.extensions
    assert "sphinxawesome_theme.highlighting" not in app.extensions
    assert "sphinxawesome_theme.docsearch" not in app.extensions


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinxawesome_theme"],
    },
)
def test_loads_default_extensions(app: Sphinx) -> None:
    """It loads the project as theme and loads all extensions."""
    app.build()
    assert app.config.html_theme == "sphinxawesome_theme"
    assert "sphinxawesome_theme" in app.extensions
    assert "sphinxawesome_theme.jinja_functions" in app.extensions
    assert "sphinxawesome_theme.highlighting" in app.extensions
    assert "sphinxawesome_theme.html_translator" in app.extensions
    assert "sphinxawesome_theme.postprocess" in app.extensions
    assert "sphinxawesome_theme.docsearch" in app.extensions


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinxawesome_theme"],
    },
)
def test_has_default_configuration(app: Sphinx) -> None:
    """It uses default configuration settings."""
    app.build()
    assert app.config.html_awesome_headerlinks is True
    assert app.config.html_awesome_code_headers is True
    assert app.config.html_awesome_postprocessing is True
    assert app.config.html_awesome_html_translator is True
    assert app.config.html_awesome_docsearch is False
    assert app.config.html_collapsible_definitions is False
    assert app.config.docsearch_config == {}
