"""Unit tests for the HTML post-processor."""


from bs4 import BeautifulSoup
import pytest
from sphinx.application import Sphinx

from sphinxawesome_theme import postprocess


@pytest.mark.sphinx("html")
def test_get_filelist(app: Sphinx) -> None:
    """It gets the correct number of HTML files."""
    app.builder.build_all()

    html_files = postprocess._get_html_files(app.outdir)
    assert len(html_files) == 3


def test_wrap_literal_block() -> None:
    """It wraps pre.literal-blocks."""
    html = "<pre class='literal-block'>Code</pre>"

    tree = BeautifulSoup(html, "html.parser")
    postprocess._wrap_literal_blocks(tree)
    pre = tree("pre")
    assert len(pre) == 1
    assert pre[0].find_parent().name == "div"
    assert pre[0].find_parent()["class"] == ["highlight"]


def test_add_copy_button() -> None:
    """It adds a button to a div.highlight element."""
    html = "<div class='highlight'>Code</div>"

    tree = BeautifulSoup(html, "html.parser")
    postprocess._add_copy_button(tree)

    btn = tree("button")
    assert len(btn) == 1
    btn = btn[0]
    assert btn["class"] == ["copy"]
    assert btn["aria-label"] == "Copy this code block"
    svg = btn("svg")
    assert svg[0]["aria-hidden"] == "true"


def test_collapsible_nav() -> None:
    """It adds a span to nested links."""
    html = """<nav>
                <ul>
                  <li><a>Link 1</a>
                    <ul>
                      <li><a>Sublink1</a></li>
                      <li><a>Sublink2</a></li>
                    </ul>
                    <li><a>Link 2</a></li>
                </ul>
            </nav>
    """

    tree = BeautifulSoup(html, "html.parser")
    postprocess._collapsible_nav(tree)

    spans = tree("span")
    assert len(spans) == 1
    assert spans[0]["class"] == ["expand"]
    assert spans[0].string == "\u25be"
    assert spans[0].previous_sibling.string == "Link 1"
