"""Tests for collapsible definition lists.

When the option ``html_collapsible_definitions``
is ``True``, some HTML classes should be added
to some definition lists but not all of them.
"""

from bs4 import BeautifulSoup
import pytest
from sphinx.application import Sphinx


def parse_html(filename: str) -> BeautifulSoup:
    """Parse an HTML file into a BeautifulSoup tree."""
    with open(filename) as file_handle:
        tree = BeautifulSoup(file_handle, "html.parser")
    return tree


@pytest.mark.sphinx(
    "html",
    testroot="collapsible",
    confoverrides={"html_theme": "sphinxawesome_theme", "html_add_permalinks": False},
)
def test_no_permalinks(app: Sphinx) -> None:
    """It tests that there are no permalinks."""
    app.build()
    tree = parse_html(app.outdir / "index.html")
    dl = tree("dl")
    assert len(dl) == 2
    headerlinks = tree("a", class_="headerlink")
    assert len(headerlinks) == 0


@pytest.mark.sphinx(
    "html",
    testroot="collapsible",
    confoverrides={"html_theme": "sphinxawesome_theme"},
    freshenv=True,
)
def test_no_collapsible_definitions(app: Sphinx) -> None:
    """By default, no classes should be added."""
    app.build()
    tree = parse_html(app.outdir / "index.html")
    dl = tree("dl")
    assert len(dl) == 2

    assert str(dl[0]).replace("\n", "") == (
        '<dl class="simple"><dt>term</dt><dd><p>definition</p></dd></dl>'
    )

    assert str(dl[1]).replace("\n", "") == (
        '<dl class="std option code-definition">'
        '<dt id="cmdoption-t">'
        '<code class="sig-name descname">-t</code>'
        '<code class="sig-prename descclassname"></code>'
        '<a aria-label="Copy link to this definition." '
        'class="headerlink tooltipped tooltipped-ne" '
        'href="#cmdoption-t" role="button">'
        '<svg pointer-events="none" viewbox="0 0 24 24" '
        'xmlns="http://www.w3.org/2000/svg"><path d="M3.9 12c0-1.71 '
        "1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 "
        "5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 "
        "13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 "
        '3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z">'
        "</path></svg></a></dt><dd><p>test</p></dd></dl>"
    )


@pytest.mark.sphinx(
    "html",
    testroot="collapsible",
    confoverrides={"html_theme": "sphinxawesome_theme"},
    freshenv=True,
)
def test_collapsible_definitions(app: Sphinx) -> None:
    """It tests the correct classes being added to the definition lists.

    It should not add the classes to normal definition lists.
    """
    # if specified in 'confoverrides', this returns a warning
    app.config.html_collapsible_definitions = True
    app.config.html_add_permalinks = "a"
    app.build()
    tree = parse_html(app.outdir / "index.html")
    dl = tree("dl")

    assert len(dl) == 2
    assert str(dl[0]).replace("\n", "") == (
        '<dl class="simple"><dt>term</dt><dd><p>definition</p></dd></dl>'
    )
    assert "code-definition" in dl[1]["class"]
    dt, dd = [c for c in dl[1].children if c.strip is None]
    assert dt.name == "dt"
    assert dt["class"] == ["accordion"]
    assert dd.name == "dd"
    assert dd["class"] == ["panel"]

    expand_more_button = dt("button", class_="expand-more")
    assert len(expand_more_button) == 1
