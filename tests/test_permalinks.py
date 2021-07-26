"""Tests for permalinks.

This tests for the correct permalink behavior
except headings, which are tested in ``test_headerlinks.py``
"""

from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .util import parse_html


@pytest.mark.sphinx(
    "html",
    testroot="table",
    freshenv=True,
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_no_permalinks_on_tables(app: Sphinx) -> None:
    """It tests parsing a table without headerlinks."""
    app.config.html_permalinks = False  # type: ignore[attr-defined]
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    tables = tree("table")
    assert len(tables) == 2
    headerlinks = tree("a", class_="headerlink")
    assert len(headerlinks) == 0


@pytest.mark.sphinx(
    "html",
    testroot="figure",
    freshenv=True,
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_no_permalinks_on_figures(app: Sphinx) -> None:
    """It tests parsing a figure without headerlinks."""
    app.config.html_permalinks = False  # type: ignore[attr-defined]
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    figures = tree("figure")
    assert len(figures) == 3
    headerlinks = tree("a", class_="headerlink")
    assert len(headerlinks) == 0


@pytest.mark.sphinx("html", testroot="table", freshenv=True)
def test_permalink_table_default_theme(app: Sphinx) -> None:
    """Test the permalink behavior in Tables.

    This uses the default theme ``alabaster`` for
    a baseline of the expected Sphinx behavior.
    """
    app.build()

    tree = parse_html(Path(app.outdir) / "index.html")

    tables = tree("table")
    assert len(tables) == 2
    assert tables[0]["id"] == "id1"
    assert tables[1]["id"] == "id2"

    for i, table in enumerate(tables, 1):
        assert table["id"] == f"id{i}"
        # filter newline characters
        children = [c for c in table.children if c.strip is None]
        caption = children[0]
        assert str(caption) == (
            '<caption><span class="caption-text">Table</span>'
            f'<a class="headerlink" href="#id{i}" '
            'title="Permalink to this table">¶</a></caption>'
        )

    # the second table has an explicit label:
    # <span id="foo"><table ...>
    span = tables[1].previous_element
    assert span.name == "span"
    assert span["id"] == "foo"


@pytest.mark.sphinx(
    "html",
    testroot="table",
    freshenv=True,
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_permalink_table_awesome_theme(app: Sphinx) -> None:
    """Test the permalink behavior in Tables.

    This uses the awesome theme.
    """
    app.build()

    tree = parse_html(Path(app.outdir) / "index.html")

    tables = tree("table")
    assert tables[0]["id"] == "id1"
    assert tables[1]["id"] == "id2"

    for i, table in enumerate(tables, 1):
        assert table["id"] == f"id{i}"
        # filter newline characters
        children = [c for c in table.children if c.strip is None]
        caption = children[0]
        assert caption.name == "caption"
        span, link = list(caption.children)
        assert span["class"] == ["caption-text"]
        assert link["class"] == ["headerlink", "tooltipped", "tooltipped-ne"]
        assert link["href"] == f"#id{i}"
        assert link["data-controller"] == "clipboard"
        assert link["data-action"] == "click->clipboard#copyHeaderLink"

    # the second table has an explicit label:
    # <span id="foo"><table ...>
    span = tables[1].previous_element
    assert span.name == "span"
    assert span["id"] == "foo"


@pytest.mark.sphinx("html", testroot="figure", freshenv=True)
def test_permalink_figure_default_theme(app: Sphinx) -> None:
    """It tests the permalink behavior in figures.

    This test uses the default ``alabaster`` theme
    to get a good baseline.
    """
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    figures = tree("figure")
    assert len(figures) == 3
    assert figures[0]["id"] == "id1"
    assert figures[0]["class"] == ["align-default"]
    assert figures[1]["id"] == "id2"
    assert figures[1]["class"] == ["align-default"]
    # figure 3 has no alt text, hence no id
    assert "id" not in figures[2].attrs

    # check the structure for figure 1, first strip newlines
    children = [c for c in figures[0].children if c.strip is None]
    assert len(children) == 2
    assert children[0].name == "img"
    assert children[1].name == "figcaption"

    # check the structure for figure 2, first strip newlines
    children = [c for c in figures[1].children if c.strip is None]
    assert len(children) == 3
    # the explicit label is inserted before the img
    assert children[0].name == "span"
    assert children[0]["id"] == "foo"
    assert children[1].name == "img"
    assert children[2].name == "figcaption"

    captions = tree("figcaption")
    assert len(captions) == 2

    for caption in captions:
        children = [c for c in caption.children if c.strip is None]
        assert len(children) == 2
        assert children[0].name == "p"
        assert children[1].name == "div"
        assert children[1]["class"] == ["legend"]


@pytest.mark.sphinx(
    "html",
    testroot="figure",
    freshenv=True,
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_permalink_figure_awesome_theme(app: Sphinx) -> None:
    """It tests the permalink behavior in figures.

    This test uses the awesome theme.
    """
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    figures = tree("figure")
    assert len(figures) == 3
    assert figures[0]["id"] == "id1"
    assert figures[1]["id"] == "id2"
    # figure 3 has no alt text, hence no id
    assert "id" not in figures[2].attrs

    # check the structure for figure 1, first strip newlines
    children = [c for c in figures[0].children if c.strip is None]
    assert len(children) == 2
    assert children[0].name == "img"
    assert children[1].name == "figcaption"

    # check the structure for figure 2, first strip newlines
    children = [c for c in figures[1].children if c.strip is None]
    assert len(children) == 3
    # the explicit label is inserted before the img
    assert children[0].name == "span"
    assert children[0]["id"] == "foo"
    assert children[1].name == "img"
    assert children[2].name == "figcaption"

    captions = tree("figcaption")
    assert len(captions) == 2

    for i, caption in enumerate(captions, 1):
        children = [c for c in caption.children if c.strip is None]
        assert len(children) == 3
        assert children[0].name == "span"
        assert children[0]["class"] == ["caption-text"]
        assert children[1].name == "a"
        assert children[1]["href"] == f"#id{i}"
        assert children[1]["aria-label"] == "Copy link to this image."
        assert children[2].name == "div"
        assert children[2]["class"] == ["legend"]


@pytest.mark.sphinx(
    "html",
    testroot="figure",
    freshenv=True,
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_figure_attributes(app: Sphinx) -> None:
    """It tests if width and align attributes are passed."""
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    figures = tree("figure")
    assert len(figures) == 3
    assert figures[2].attrs["class"] == ["align-left"]
    assert figures[2].attrs["style"] == "width: 99%"
    img = figures[2].find("img")
    assert img.attrs["width"] == "50%"


@pytest.mark.sphinx(
    "html",
    testroot="toctree",
    freshenv=True,
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_caption_on_toctree(app: Sphinx) -> None:
    """It tests parsing a table without headerlinks."""
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    captions = tree("p", class_="caption")
    assert len(captions) == 2
    for cap in captions:
        assert cap.text == "Foo"
