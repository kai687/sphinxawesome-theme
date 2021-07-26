"""Tests for codeblocks.

Since the structure of the codeblock is quite
different from the default there isn't much
point in comparing the awesome theme to the
default, but it'll still be a good reference
for the default and to catch, if something
has changed.
"""
import os
from pathlib import Path

import pytest
from sphinx.application import Sphinx
from sphinx.testing.util import etree_parse

from .util import parse_html


@pytest.mark.sphinx(
    "xml",
    testroot="code",
    confoverrides={"extensions": ["sphinxawesome_theme"]},
    freshenv=True,
)
def test_doctree_awesome_theme(app: Sphinx) -> None:
    """It tests the correct structure of the doctree."""
    app.build()
    tree = etree_parse(os.path.join(app.outdir, "index.xml"))
    code_blocks = tree.findall(".//literal_block")

    assert len(code_blocks) == 8

    # first block is without anything
    assert code_blocks[0].attrib["language"] == "default"
    assert "ids" not in code_blocks[0].attrib
    assert "names" not in code_blocks[0].attrib

    # second block has an explicit ID
    assert code_blocks[1].attrib["language"] == "default"
    assert code_blocks[1].attrib["ids"] == "foo"
    assert code_blocks[1].attrib["names"] == "foo"

    # third block is inside a container (test later)
    assert code_blocks[2].attrib["language"] == "python"
    assert "ids" not in code_blocks[2].attrib
    assert "names" not in code_blocks[2].attrib

    # fourth block is inside container AND has explicit label
    # the ids are applied to the container, so it looks exactly
    # like the third block
    assert code_blocks[3].attrib["language"] == "python"
    assert "ids" not in code_blocks[2].attrib
    assert "names" not in code_blocks[2].attrib

    # fifth block has linenumbers enabled
    assert code_blocks[4].attrib["linenos"] == "True"

    # sixth block has emphasized lines
    assert code_blocks[5].attrib["highlight_args"] == "{'hl_lines': [1]}"

    # seventh block has added/removed lines
    assert code_blocks[6].attrib["highlight_args"] == (
        "{'hl_added': [1], 'hl_removed': [2]}"
    )

    # container wrappers
    containers = tree.findall(".//container")
    assert len(containers) == 3

    assert containers[0].attrib["classes"] == "highlight"
    assert containers[1].attrib["classes"] == "highlight"
    assert containers[2].attrib["classes"] == "bogus"

    assert containers[0].attrib["language"] == "python"
    assert containers[1].attrib["language"] == "python"
    assert "language" not in containers[2].attrib

    assert containers[0].attrib["literal_block"] == "True"
    assert containers[1].attrib["literal_block"] == "True"
    assert "literal_block" not in containers[2].attrib

    assert containers[0].attrib["ids"] == "id1"
    assert "names" not in containers[0].attrib
    assert containers[1].attrib["ids"] == "id2 bar"
    assert containers[1].attrib["names"] == "bar"
    assert "names" not in containers[2].attrib

    # should have two children
    assert len(containers[0]) == len(containers[1]) == 2
    assert containers[0][0].tag == "caption"
    assert containers[0][0].text == "test"
    assert containers[0][1].tag == "literal_block"
    assert containers[1][0].tag == "caption"
    assert containers[1][0].text == "test"
    assert containers[1][1].tag == "literal_block"


@pytest.mark.sphinx(
    "html",
    testroot="code",
    freshenv=True,
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_no_permalinks_on_codeblocks(app: Sphinx) -> None:
    """It tests codeblocks without headerlinks."""
    app.config.html_permalinks = False  # type: ignore[attr-defined]
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    code_blocks = tree("div", class_="highlight")
    assert len(code_blocks) == 8
    code_headers = tree("div", class_="code-header")
    assert len(code_headers) == 8
    headerlinks = tree("a", class_="headerlink")
    assert len(headerlinks) == 0


@pytest.mark.skip(reason="Flaky test.")
@pytest.mark.sphinx("html", testroot="code", freshenv=True)
def test_basic_codeblock_default_theme(app: Sphinx) -> None:
    """It parses basic codeblocks with the default theme.

    By default, Pygments returns the ``div.highlight`` block.
    Sphinx wraps it in a ``div.highlight-default`` block.

    .. caution::

       This test passes on its own, but not when running in the
       test suite. It looks like the PygmentsBridge setting
       is being cached between runs and it uses the AwesomeHtmlFormatter
       in combination with default Sphinx.
    """
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")

    # blocks without caption
    default_blocks = tree("div", class_="highlight-default")
    assert len(default_blocks) == 2
    assert str(default_blocks[0]).replace("\n", "") == (
        '<div class="highlight-default notranslate">'
        '<div class="highlight"><pre><span></span>'
        '<span class="nb">print</span><span class="p">'
        '(</span><span class="s2">"Hello"</span>'
        '<span class="p">)</span></pre></div></div>'
    )
    # code block with explicit label
    assert str(default_blocks[1]).replace("\n", "") == (
        '<div class="highlight-default notranslate" id="foo">'
        '<div class="highlight"><pre><span></span>'
        '<span class="nb">print</span><span class="p">'
        '(</span><span class="s2">"Hello"</span>'
        '<span class="p">)</span></pre></div></div>'
    )


@pytest.mark.skip(reason="Flaky test.")
@pytest.mark.sphinx("html", testroot="code", freshenv=True)
def test_captioned_codeblocks_with_default_theme(app: Sphinx) -> None:
    """It parses codeblocks with captions using the default theme.

    The ``div.highlight-default`` is wrapped in a ``div.literal-block-wrapper``.

    .. caution::

       This test passes on its own, but not when running in the
       test suite. It looks like the PygmentsBridge setting
       is being cached between runs and it uses the AwesomeHtmlFormatter
       in combination with default Sphinx.
    """
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    default_blocks = tree("div", class_="literal-block-wrapper")

    assert len(default_blocks) == 2
    assert default_blocks[0]["id"] == "id1"
    assert default_blocks[1]["id"] == "id2"

    children = [c for c in default_blocks[0].children if c.strip is None]

    # the first block does not have an explicit label
    assert len(children) == 2
    # first the caption div ...
    assert str(children[0]) == (
        '<div class="code-block-caption">'
        '<span class="caption-text">test</span>'
        '<a class="headerlink" href="#id1" title="Permalink to this code">¶</a></div>'
    )
    # ... then the actual code block
    assert str(children[1]).replace("\n", "") == (
        '<div class="highlight-python notranslate">'
        '<div class="highlight"><pre><span></span>'
        '<span class="nb">print</span><span class="p">'
        '(</span><span class="s2">"Hello"</span><span class="p">)'
        "</span></pre></div></div>"
    )

    children = [c for c in default_blocks[1].children if c.strip is None]

    # the second block has an explicit label
    assert len(children) == 3
    assert str(children[0]) == '<span id="bar"></span>'
    assert str(children[1]) == (
        '<div class="code-block-caption">'
        '<span class="caption-text">test</span>'
        '<a class="headerlink" href="#id2" title="Permalink to this code">¶</a></div>'
    )
    assert str(children[2]).replace("\n", "") == (
        '<div class="highlight-python notranslate">'
        '<div class="highlight"><pre><span></span>'
        '<span class="nb">print</span><span class="p">'
        '(</span><span class="s2">"Hello"</span><span class="p">)'
        "</span></pre></div></div>"
    )


@pytest.mark.sphinx(
    "html",
    testroot="code",
    freshenv=True,
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_basic_codeblock_awesome_theme(app: Sphinx) -> None:
    """It parses basic codeblocks with the awesome theme.

    With ``::`` and an indented block, the default should
    have a ``<span class="code-lang">python</span>``, and
    a copy button.

    The code block itself should come wrapped in a ``<pre><code>``.
    """
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    code_blocks = tree("div", class_="highlight")
    assert len(code_blocks) == 8
    children = [c for c in code_blocks[0].children if c.strip is None]
    assert len(children) == 2

    header, code = children
    assert header["class"] == ["code-header"]
    span, button = list(header.children)
    assert span["class"] == ["code-lang"]
    assert button["class"] == ["copy", "tooltipped", "tooltipped-nw"]
    assert button["data-controller"] == "clipboard"
    assert button["data-action"] == "clipboard#copyCodeBlock"
    assert len(button.children) == 1
    icon = button.children[0]
    assert icon.name == "svg"
    assert str(code) == (
        '<pre><code><span class="nb">print</span>'
        '<span class="p">(</span><span class="s2">"Hello"</span>'
        '<span class="p">)</span>\n'
        "</code></pre>"
    )
    # explicit label before code block gets turned into
    # an ID on the ``div.highlight``.
    assert code_blocks[1]["id"] == "foo"


@pytest.mark.sphinx(
    "html",
    testroot="code",
    freshenv=True,
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_captioned_codeblocks_with_awesome_theme(app: Sphinx) -> None:
    """It parses a codeblock with captions."""
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    code_blocks = tree("div", class_="highlight")
    code_header = code_blocks[2].find_all("div", class_="code-header")
    assert len(code_header) == 1

    # remove newline characters
    children = [c for c in code_header[0].children if c.strip is None]
    assert len(children) == 3
    assert str(children[0]) == '<span class="code-lang">python</span>'

    caption = children[1]
    assert caption.name == "span"
    caption_text, link = caption.children
    assert caption_text["class"] == ["caption-text"]
    assert link["aria-label"] == ["Copy link to this code block"]
    assert link["data-controller"] == "clipboard"
    assert link["data-action"] == "click->clipboard#copyHeaderLink"

    copy_code = children[2]
    assert copy_code["aria-label"] == "Copy this code"
    assert copy_code["data-controller"] == "clipboard"
    assert "copy" in copy_code["class"]
    assert copy_code["data-action"] == "clipboard#copyCodeBlock"


@pytest.mark.sphinx(
    "html",
    testroot="code",
    freshenv=True,
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_codeblocks_with_linenumbers_awesome_theme(app: Sphinx) -> None:
    """It highlights codeblock with inline linenumbers."""
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    code_blocks = tree("div", class_="highlight")
    block = code_blocks[4]
    code = block.select("pre > code")
    assert len(code) == 1
    assert str(code[0]).replace("\n", "") == (
        '<code><span class="code-line" '
        'id="line-1"><span class="linenos">1</span>'
        '<span class="nb">print</span><span class="p">'
        '(</span><span class="s2">"Hello"</span>'
        '<span class="p">)</span></span></code>'
    )


@pytest.mark.sphinx(
    "html",
    testroot="code",
    freshenv=True,
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_codeblocks_with_emph_lines_awesome_theme(app: Sphinx) -> None:
    """It highlights codeblock with emphasized lines."""
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    code_blocks = tree("div", class_="highlight")
    block = code_blocks[5]
    mark = block.select("pre > code > mark")
    assert len(mark) == 1
    assert str(mark[0]).replace("\n", "") == (
        '<mark><span class="nb">print</span><span class="p">'
        '(</span><span class="s2">"Hello"</span><span class="p">)'
        "</span></mark>"
    )


@pytest.mark.sphinx(
    "html",
    testroot="code",
    freshenv=True,
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_codeblocks_with_added_removed_lines_awesome_theme(app: Sphinx) -> None:
    """It highlights codeblocks with added and removed lines."""
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    code_blocks = tree("div", class_="highlight")
    block = code_blocks[6]
    code = block.select("pre > code")
    assert len(code) == 1
    assert str(code[0]).replace("\n", "") == (
        '<code><ins><span class="nb">print</span>'
        '<span class="p">(</span><span class="s2">"Added"</span>'
        '<span class="p">)</span></ins>'
        '<del><span class="nb">print</span><span class="p">'
        '(</span><span class="s2">"Removed"</span>'
        '<span class="p">)</span></del></code>'
    )


@pytest.mark.sphinx(
    "html",
    testroot="code",
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_non_literal_container(app: Sphinx) -> None:
    """It transforms a container node that isn't a code block."""
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    container_nodes = tree("div", class_="bogus")
    assert len(container_nodes) == 1
    assert str(container_nodes[0]).replace("\n", "") == (
        '<div class="bogus docutils container"><p>Doesn’t do much.</p></div>'
    )


@pytest.mark.sphinx(
    "html",
    testroot="code",
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_parsed_literal(app: Sphinx) -> None:
    """It transforms a parsed literal directive correctly."""
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    literal = tree("div", class_="highlight")

    assert len(literal) == 8
    assert str(literal[7]).replace("\n", "") == (
        '<div class="highlight"><div class="code-header">'
        '<button aria-label="Copy this code" class="copy tooltipped tooltipped-nw">'
        '<svg aria-hidden="true" viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/xvg">'  # noqa: E501,B950
        '<path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 '
        '1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z">'
        "</path></svg></button>"
        "</div><pre><code><em>Markup</em></code></pre></div>"
    )
