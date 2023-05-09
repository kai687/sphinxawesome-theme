"""Test the loading of the awesome extensions."""

import os
import re
from io import StringIO
from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .util import parse_html


@pytest.mark.sphinx("html", confoverrides={"html_theme": "sphinxawesome_theme"})
def test_compiles_html_with_theme(app: Sphinx) -> None:
    """It compiles HTML with the theme but doesn't load the extra extensions."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    assert app.config.html_theme == "sphinxawesome_theme"

    assert "sphinxawesome_theme.highlighting" not in app.extensions
    assert app.config.html_awesome_highlighting is True
    assert "sphinxawesome_theme.jinja_functions" in app.extensions
    assert "sphinxawesome_theme.docsearch" not in app.extensions
    assert "sphinxawesome_theme.postprocess" not in app.extensions
    assert app.config.html_awesome_postprocessing is True
    assert app.config.html_awesome_code_headers is True


@pytest.mark.sphinx("html", confoverrides={"extensions": ["sphinxawesome_theme"]})
def test_internal_extensions(app: Sphinx) -> None:
    """It sets up all internal Sphinx extensions when loaded as an extension."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    assert app.config.html_theme == "alabaster"
    assert "sphinxawesome_theme.highlighting" in app.extensions
    assert "sphinxawesome_theme.jinja_functions" in app.extensions
    assert "sphinxawesome_theme.postprocess" in app.extensions
    assert app.config.html_awesome_highlighting is True
    assert app.config.html_awesome_postprocessing is True
    assert app.config.html_awesome_code_headers is True


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "extensions": ["sphinxawesome_theme"],
        "html_awesome_postprocessing": False,
        "html_awesome_code_headers": False,
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
        "extensions": ["sphinxawesome_theme.docsearch"],
    },
)
def test_awesome_docsearch(app: Sphinx, warning: StringIO) -> None:
    """It loads the awesome DocSearch extension."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    assert "sphinxawesome_theme.docsearch" in app.extensions

    tree = parse_html(Path(app.outdir) / "index.html")
    pattern = re.compile(r"docsearch\.[0-9a-z]+\.(css|js)")

    # It adds the `docsearch.css` file
    css = tree.select('link[rel="stylesheet"]')
    assert len(css) == 3
    hrefs = [item["href"] for item in css]
    assert any(filter(pattern.search, hrefs))  # type: ignore[arg-type]

    # It adds the `docsearch.js` file
    scripts = tree.select("script")
    assert len(scripts) == 4
    print("SCRIPTS: ", scripts)
    script_src = [item["src"] for item in scripts if "src" in item.attrs]
    assert any(filter(pattern.search, script_src))  # type: ignore[arg-type]

    warnings = warning.getvalue()
    assert (
        "You must provide your Algolia application ID for DocSearch to work."
        in warnings
    )
    assert (
        "You must provide your Algolia search API key for DocSearch to work."
        in warnings
    )
    assert "You must provide your Algolia index name for DocSearch to work." in warnings


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinxawesome_theme.docsearch"],
        "docsearch_app_id": "test",
        "docsearch_api_key": "test",
        "docsearch_index_name": "test",
    },
)
def test_docsearch_no_warnings(app: Sphinx, warning: StringIO) -> None:
    """It compiles without warnings."""
    app.build()
    warnings = warning.getvalue()
    assert len(warnings) == 0


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinxawesome_theme", "sphinx_design"],
    },
)
def test_awesome_sphinx_design(app: Sphinx) -> None:
    """It loads CSS for the `sphinx-design` extension."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    tree = parse_html(Path(app.outdir) / "index.html")
    pattern = re.compile(r"awesome-sphinx-design\.[0-9a-z]+\.(css|js)")

    # It adds the `awesome-sphinx-design.css` file
    css = tree.select('link[rel="stylesheet"]')
    assert len(css) == 4
    hrefs = [item["href"] for item in css]
    assert any(filter(pattern.search, hrefs))  # type: ignore[arg-type]
