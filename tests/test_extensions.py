"""Test the loading of the awesome extensions."""

import os
import re
from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .util import parse_html


@pytest.mark.sphinx("html", confoverrides={"html_theme": "sphinxawesome_theme"})
def test_compiles_html_with_theme(app: Sphinx) -> None:
    """It compiles HTML with the theme without having to load it as extension."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    assert app.config.html_theme == "sphinxawesome_theme"
    assert "sphinxawesome_theme.html_translator" not in app.extensions
    assert app.config.html_awesome_html_translator is True
    assert "sphinxawesome_theme.highlighting" not in app.extensions
    assert app.config.html_awesome_highlighting is True
    assert "sphinxawesome_theme.jinja_functions" in app.extensions
    assert "sphinxawesome_theme.docsearch" not in app.extensions
    assert app.config.html_awesome_docsearch is False
    assert "sphinxawesome_theme.postprocess" not in app.extensions
    assert app.config.html_awesome_postprocessing is True
    assert app.config.html_awesome_code_headers is True
    assert app.config.html_awesome_headerlinks is True
    assert app.config.html_collapsible_definitions is False


@pytest.mark.sphinx("html", confoverrides={"extensions": ["sphinxawesome_theme"]})
def test_internal_extensions(app: Sphinx) -> None:
    """It sets up all internal Sphinx extensions when loaded as an extension."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    assert app.config.html_theme == "alabaster"
    assert "sphinxawesome_theme.html_translator" in app.extensions
    assert app.config.html_awesome_html_translator is True
    assert "sphinxawesome_theme.highlighting" in app.extensions
    assert app.config.html_awesome_highlighting is True
    assert "sphinxawesome_theme.jinja_functions" in app.extensions
    assert "sphinxawesome_theme.docsearch" not in app.extensions
    assert app.config.html_awesome_docsearch is False
    assert "sphinxawesome_theme.postprocess" in app.extensions
    assert app.config.html_awesome_postprocessing is True
    assert app.config.html_awesome_code_headers is True
    assert app.config.html_awesome_headerlinks is True
    assert app.config.html_collapsible_definitions is False


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "extensions": ["sphinxawesome_theme"],
        "html_awesome_html_translator": False,
    },
)
def test_no_awesome_html_translator(app: Sphinx) -> None:
    """It doesn't load the awesome HTML translator."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    assert "sphinxawesome_theme.html_translator" not in app.extensions
    assert app.config.html_awesome_html_translator is False


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "extensions": ["sphinxawesome_theme"],
        "html_awesome_postprocessing": False,
    },
)
def test_no_awesome_postprocessing(app: Sphinx) -> None:
    """It doesn't load the awesome postprocessing extension."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    assert "sphinxawesome_theme.postprocessing" not in app.extensions
    assert app.config.html_awesome_postprocessing is False


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinxawesome_theme"],
        "html_awesome_docsearch": True,
    },
)
def test_awesome_docsearch(app: Sphinx) -> None:
    """It loads the awesome DocSearch extension."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    assert "sphinxawesome_theme.docsearch" in app.extensions
    assert app.config.html_awesome_docsearch is True

    tree = parse_html(Path(app.outdir) / "index.html")
    pattern = re.compile(r"docsearch\.[0-9a-z]+\.(css|js)")

    # It adds the `docsearch.css` file
    css = tree.select('link[rel="stylesheet"]')
    assert len(css) == 3
    hrefs = [item["href"] for item in css]
    assert any(filter(pattern.search, hrefs))  # type: ignore[arg-type]

    # It adds the `docsearch.js` file
    scripts = tree.select("script")
    assert len(scripts) == 3
    script_src = [item["src"] for item in scripts]
    assert any(filter(pattern.search, script_src))  # type: ignore[arg-type]
