"""Unit tests for the HTML post-processor."""


from bs4 import BeautifulSoup
import pytest
from sphinx.application import Sphinx

from sphinxawesome_theme import postprocess


def parse_html(html: str) -> BeautifulSoup:
    """Take a HTML as string and return a BeautifulSoup tree."""
    return BeautifulSoup(html, "html.parser")


@pytest.mark.sphinx("html")
def test_get_filelist(app: Sphinx) -> None:
    """It gets the correct number of HTML files."""
    app.builder.build_all()

    html_files = postprocess._get_html_files(app.outdir)
    assert len(html_files) == 3


def test_collapsible_nav() -> None:
    """It adds a span to nested links."""
    html = """
        <nav class="nav-toc">
            <ul>
                <li>
                    <a>Link 1</a>
                    <ul>
                      <li><a>Sublink1</a></li>
                      <li><a>Sublink2</a></li>
                    </ul>
                </li>
                <li><a>Link 2</a></li>
            </ul>
        </nav>
    """

    tree = parse_html(html)
    postprocess._collapsible_nav(tree)

    icons = tree("svg")
    assert len(icons) == 1
    assert icons[0]["class"] == ["expand"]
    assert icons[0].next_sibling.string == "Link 1"


def test_expand_current() -> None:
    """It adds a class to a li.current but not other li."""
    tree = parse_html("<li class='current'>current</li>")
    postprocess._expand_current(tree)
    assert "expanded" in tree.li["class"]

    tree = parse_html("<li>No current</li>")
    postprocess._expand_current(tree)
    assert not tree.li.has_attr("class")
