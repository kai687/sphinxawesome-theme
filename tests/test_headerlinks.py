"""Tests for headerlinks.

We want to make sure, that all modifications
to the headerlink behavior are intended.

We also test against the default ``alabaster``
theme. This allows us to see, if anything changed
in the default Sphinx implementation, that might
require changes from me.
"""

import re

from bs4 import BeautifulSoup
import pytest
from sphinx.application import Sphinx


def parse_html(filename: str) -> BeautifulSoup:
    """Parse an HTML file into a BeautifulSoup tree."""
    with open(filename) as file_handle:
        tree = BeautifulSoup(file_handle, "html.parser")
    return tree


@pytest.mark.sphinx("html", testroot="headerlinks", freshenv=True)
def test_headerlink_with_default_theme(app: Sphinx) -> None:
    """It tests the default structure of a headerlink.

    This uses the default theme ``alabaster``.

    We want to have a baseline against which we can compare
    our modifications.
    """
    app.build()
    tree = parse_html(app.outdir / "index.html")
    headings = tree.find_all(re.compile("^h[1..2]"), class_=None)
    assert len(headings) == 4

    h1 = headings[0]
    assert str(h1) == (
        '<h1>Test<a class="headerlink" '
        'href="#test" '
        'title="Permalink to this headline">¶</a></h1>'
    )
    h1 = headings[1]
    assert str(h1) == (
        '<h1>Second Test<a class="headerlink" '
        'href="#second-test" '
        'title="Permalink to this headline">¶</a></h1>'
    )
    h2 = headings[2]
    assert str(h2) == (
        '<h2><a class="toc-backref" '
        'href="#id1">Third Test</a>'
        '<a class="headerlink" href="#third-test" '
        'title="Permalink to this headline">¶</a></h2>'
    )
    h2 = headings[3]
    assert str(h2) == (
        '<h2><a class="toc-backref" '
        'href="#id2">Fourth Test</a>'
        '<a class="headerlink" href="#fourth-test" '
        'title="Permalink to this headline">¶</a></h2>'
    )


@pytest.mark.sphinx("html", testroot="headerlinks", freshenv=True)
def test_ids_with_default_theme(app: Sphinx) -> None:
    """It tests section IDs.

    This uses the default theme ``alabaster``.

    We want to have a baseline against which we can compare
    our modifications.
    """
    app.build()
    tree = parse_html(app.outdir / "index.html")
    sections = tree("div", class_="section")
    assert len(sections) == 4
    assert sections[0]["id"] == "test"
    assert sections[1]["id"] == "second-test"
    assert sections[2]["id"] == "third-test"
    assert sections[3]["id"] == "fourth-test"


@pytest.mark.sphinx(
    "html",
    testroot="headerlinks",
    freshenv=True,
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_headerlink_with_awesome_theme(app: Sphinx) -> None:
    """It tests the structure of a headerlink.

    Using the Sphinxawesome theme.
    """
    app.build()
    tree = parse_html(app.outdir / "index.html")
    headings = tree.find_all(re.compile("^h[1..2]"), class_=None)
    assert len(headings) == 4

    h1 = headings[0]
    assert str(h1) == (
        '<h1>Test<a aria-label="Copy link to section: Test." '
        'class="headerlink tooltipped tooltipped-ne" '
        'href="#test" role="button"><svg pointer-events="none" '
        'viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
        '<path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 '
        "0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 "
        "13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 "
        '3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"></path>'
        "</svg></a></h1>"
    )
    h1 = headings[1]
    assert str(h1) == (
        '<h1>Second Test<a aria-label="Copy link to section: Second Test." '
        'class="headerlink tooltipped tooltipped-ne" href="#second-test" '
        'role="button"><svg pointer-events="none" viewbox="0 0 24 24" '
        'xmlns="http://www.w3.org/2000/svg"><path d="M3.9 12c0-1.71 '
        "1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 "
        "5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 "
        "13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 "
        '3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"></path>'
        "</svg></a></h1>"
    )
    h2 = headings[2]
    assert str(h2) == (
        '<h2><a class="toc-backref" href="#id1">Third Test</a>'
        '<a aria-label="Copy link to this section: Third Test" '
        'class="headerlink tooltipped tooltipped-ne" href="#third-test" '
        'role="button"><svg pointer-events="none" viewbox="0 0 24 24" '
        'xmlns="http://www.w3.org/2000/svg"><path d="M3.9 12c0-1.71 '
        "1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 "
        "5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 "
        "0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 "
        '5-5s-2.24-5-5-5z"></path></svg></a></h2>'
    )
    h2 = headings[3]
    assert str(h2) == (
        '<h2><a class="toc-backref" href="#id2">Fourth Test</a>'
        '<a aria-label="Copy link to this section: Fourth Test" '
        'class="headerlink tooltipped tooltipped-ne" '
        'href="#fourth-test" role="button"><svg pointer-events="none" '
        'viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
        '<path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 '
        "2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 "
        "13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 "
        '3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z">'
        "</path></svg></a></h2>"
    )


@pytest.mark.sphinx(
    "html",
    testroot="headerlinks",
    freshenv=True,
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_ids_with_awesome_theme(app: Sphinx) -> None:
    """It tests section IDs.

    Apart from using 'section' instead of 'div.section',
    the result should be the same.
    """
    app.build()
    tree = parse_html(app.outdir / "index.html")
    sections = tree("section")
    # there is <section role="contentinfo"> at the bottom.
    assert len(sections) == 5
    assert sections[0]["id"] == "test"
    assert sections[1]["id"] == "second-test"
    assert sections[2]["id"] == "third-test"
    assert sections[3]["id"] == "fourth-test"
