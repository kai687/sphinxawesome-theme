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


def test_wrap_literal_block() -> None:
    """It wraps pre.literal-blocks."""
    tree = parse_html("<pre class='literal-block'>Code</pre>")
    postprocess._wrap_literal_blocks(tree)
    pre = tree("pre")
    assert len(pre) == 1
    assert pre[0].find_parent().name == "div"
    assert pre[0].find_parent()["class"] == ["highlight"]


def test_add_copy_button() -> None:
    """It adds a button to a div.highlight element."""
    tree = parse_html("<div class='highlight'>Code</div>")
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
    html = """<div id="nav-toc">
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
            </div>
    """

    tree = parse_html(html)
    postprocess._collapsible_nav(tree)

    spans = tree("span")
    assert len(spans) == 1
    assert spans[0]["class"] == ["expand"]
    assert spans[0].string == "\u203a"
    assert spans[0].next_sibling.string == "Link 1"


def test_div_to_section() -> None:
    """It converts div.section to section."""
    tree = parse_html("<div class='section'>Something</div>")
    postprocess._divs_to_section(tree)
    divs = tree("div")
    assert len(divs) == 0
    sections = tree("section")
    assert len(sections) == 1
    assert not sections[0].has_attr("class")


def test_div_to_fig() -> None:
    """It converts a div.figure into figure element and p.caption into figcaption."""
    tree = parse_html("<div class='figure'><p class='caption'>Caption</p></div>")
    postprocess._divs_to_figure(tree)
    assert not tree("div")
    assert not tree("p")
    assert tree("figure")
    assert tree("figcaption")


def test_div_to_fig_no_caption() -> None:
    """It converts a div.figure without caption into figure."""
    tree = parse_html("<div class='figure'>image</div>")
    postprocess._divs_to_figure(tree)
    assert not tree("div")
    assert tree("figure")
    assert tree.figure.string == "image"


def test_expand_current() -> None:
    """It adds a class to a li.current but not other li."""
    tree = parse_html("<li class='current'>current</li>")
    postprocess._expand_current(tree)
    assert "expanded" in tree.li["class"]

    tree = parse_html("<li>No current</li>")
    postprocess._expand_current(tree)
    assert not tree.li.has_attr("class")


def test_remove_pre_spans() -> None:
    """It removes unneeded span.pre elements inside inline code."""
    tree = parse_html("<code><span class='pre'>code</span></code>")
    postprocess._remove_pre_spans(tree)
    assert not tree("span")
    assert len(list(tree.code.children)) == 1
    assert tree.code.string == "code"


@pytest.mark.sphinx("html", confoverrides={"html_theme": "sphinxawesome_theme"})
def test_modify_html(app: Sphinx) -> None:
    """It performs all transforms."""
    app.builder.build_all()
    postprocess._modify_html(app.outdir / "index.html", app.config)

    assert (app.outdir / "index.html").exists()


@pytest.mark.sphinx("html", confoverrides={"html_theme": "sphinxawesome_theme"})
def test_postprocess_html(app: Sphinx) -> None:
    """It performs all transforms."""
    app.builder.build_all()
    postprocess.post_process_html(app, None)
    assert (app.outdir / "index.html").exists()


@pytest.mark.sphinx("xml", confoverrides={"html_theme": "sphinxawesome_theme"})
def test_dont_postprocess_xml(app: Sphinx) -> None:
    """It skips the XML builder."""
    app.builder.build_all()
    postprocess.post_process_html(app, None)
    assert app.builder.name == "xml"
    # not sure how I can properly test this branch
    assert (app.outdir / "index.xml").exists()

    postprocess.post_process_html(app, Exception())
