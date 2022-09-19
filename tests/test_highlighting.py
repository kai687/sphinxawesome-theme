"""Test the loading of the awesome extensions."""

import os
from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .util import parse_html


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "extensions": ["sphinxawesome_theme"],
        "html_awesome_highlighting": False,
    },
)
def test_no_awesome_highlighting(app: Sphinx) -> None:
    """It doesn't load the awesome highlighting extension."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    assert "sphinxawesome_theme.highlighting" not in app.extensions
    assert app.config.html_awesome_highlighting is False


@pytest.mark.sphinx(
    "html",
    testroot="highlighting",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinxawesome_theme"],
    },
)
def test_awesome_code_blocks(app: Sphinx) -> None:
    """It has all features of awesome code blocks."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    tree = parse_html(Path(app.outdir) / "index.html")

    code = tree.select(".code-wrapper")
    assert len(code) == 1

    header = code[0].select(".code-header")
    assert len(header) == 1

    lang = code[0].select(".code-lang")
    assert len(lang) == 1

    deleted = code[0]("del")
    assert len(deleted) == 1

    ins = code[0]("ins")
    assert len(ins) == 1

    mark = code[0]("mark")
    assert len(mark) == 1

    var = code[0]("var")
    assert len(var) == 1


@pytest.mark.sphinx(
    "html",
    testroot="highlighting",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinxawesome_theme"],
        "html_awesome_code_headers": False,
    },
)
def test_no_awesome_code_headers(app: Sphinx) -> None:
    """It doesn't add code headers."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    tree = parse_html(Path(app.outdir) / "index.html")

    lang = tree.select(".code-lang")
    assert len(lang) == 0
