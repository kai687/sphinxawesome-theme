"""Tests for the various theme options.

Test for the presence and absence of certain HTML elements.
"""

import re

import pytest
from bs4 import BeautifulSoup
from sphinx.application import Sphinx


def parse_html(filename: str) -> BeautifulSoup:
    """Parse an HTML file into a BeautifulSoup tree."""
    with open(filename) as file_handle:
        tree = BeautifulSoup(file_handle, "html.parser")
    return tree


def read_as_text(filename: str) -> str:
    """Read a file as text."""
    with open(filename) as file_handle:
        txt = file_handle.read()
    return txt


@pytest.mark.sphinx("html", testroot="options")
def test_default_options(app: Sphinx) -> None:
    """It tests the default settings."""
    app.build()
    tree = parse_html(app.outdir / "another.html")

    # breadcrumbs should be present
    nav = tree("nav", attrs={"aria-label": "breadcrumbs"})
    assert len(nav) == 1

    # default breadcrumbs character is ``/``
    assert "/" in nav[0].text

    # navigation menu should be present
    nav = tree.select("#sidebar > nav")
    assert len(nav) == 1

    # prev_next should not be present (doesn't have better pattern)
    txt = read_as_text(app.outdir / "another.html")
    assert not re.search("Previous", txt, re.I)
    assert not re.search("Next", txt, re.I)

    # navigation should include the 'another' document (toctree with hidden option)
    li = nav[0]("li", class_="current")
    assert len(li) == 1
    assert li[0].text == "title"


@pytest.mark.sphinx(
    "html",
    testroot="options",
    confoverrides={"html_theme_options": {"show_breadcrumbs": False}},
)
def test_no_breadcrumbs(app: Sphinx) -> None:
    """It tests deactivating the breadcrumbs theme option."""
    app.build()
    tree = parse_html(app.outdir / "another.html")
    nav = tree("nav", attrs={"aria-label": "breadcrumbs"})
    assert len(nav) == 0


@pytest.mark.sphinx(
    "html",
    testroot="options",
    confoverrides={"html_theme_options": {"breadcrumbs_separator": "$"}},
)
def test_different_breadcrumbs_character(app: Sphinx) -> None:
    """It tests using a different breadcrumbs character."""
    app.build()
    tree = parse_html(app.outdir / "another.html")
    nav = tree.find("nav", attrs={"aria-label": "breadcrumbs"})
    assert "$" in nav.text


@pytest.mark.sphinx(
    "html",
    testroot="options",
    confoverrides={"html_theme_options": {"show_nav": False}},
)
def test_no_nav(app: Sphinx) -> None:
    """It tests deactivating the navigation menu theme option."""
    app.build()
    tree = parse_html(app.outdir / "another.html")
    nav = tree.select("#sidebar > nav")
    assert len(nav) == 0


@pytest.mark.sphinx(
    "html",
    testroot="options",
    confoverrides={"html_theme_options": {"show_prev_next": True}},
    freshenv=True,
)
def test_prev_next(app: Sphinx) -> None:
    """It tests activating the previous/next links theme option."""
    app.build()
    txt = read_as_text(app.outdir / "another.html")
    assert re.search("Previous", txt, re.I)


@pytest.mark.sphinx(
    "html",
    testroot="options",
    confoverrides={"html_theme_options": {"nav_include_hidden": False}},
    freshenv=True,
)
def test_no_include_hidden(app: Sphinx) -> None:
    """It tests deactivating the ``nav_include_hidden`` option."""
    app.build()
    tree = parse_html(app.outdir / "another.html")
    nav = tree.select("#sidebar > nav")
    # navigation should include the 'another' document (toctree with hidden option)
    li = nav[0]("li", class_="current")
    assert len(li) == 0
