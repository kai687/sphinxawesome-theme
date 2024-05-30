"""Add more highlighting options to Pygments.

Provide a new Pygments HTML formatter ``AwesomeHtmlFormatter``.
This handles formatting the lines for added or removed options.
This changes the output compared to the default Sphinx implementation.
For example, each line is wrapped in a ``<span>`` element,
and the whole code block is wrapped in a ``<pre><code>..`` element.
For highlighted lines, this extension uses ``<mark>``, ``<ins>``, and ``<del>`` elements.

Define a new custom Pygments filter ``AwesomePlaceholders``,
which wraps each encountered placeholder word in a ``Generic.Emphasized`` token,
such that we can style placeholders by CSS.

:copyright: Copyright Kai Welke.
:license: MIT, see LICENSE for details.
"""

from __future__ import annotations

import re
from typing import Any, Generator, Literal, Pattern, Tuple, Union

from pygments.filter import Filter
from pygments.formatters import HtmlFormatter
from pygments.lexer import Lexer
from pygments.token import Generic, _TokenType
from pygments.util import get_list_opt
from sphinx.application import Sphinx
from sphinx.highlighting import _LATEX_ADD_STYLES, PygmentsBridge
from sphinx.util import logging

logger = logging.getLogger(__name__)

# type alias
TokenType = Union[_TokenType, int]  # For Python 3.8
TokenStream = Generator[Tuple[TokenType, str], None, None]


def _replace_placeholders(
    ttype: TokenType, value: str, regex: Pattern[str]
) -> TokenStream:
    """Replace every occurence of ``regex`` with ``Generic.Emph`` token."""
    last = 0
    for match in regex.finditer(value):
        start, end = match.start(), match.end()
        if start != last:
            yield ttype, value[last:start]
        yield Generic.Emph, value[start:end]
        last = end
    if last != len(value):
        yield ttype, value[last:]


class AwesomePlaceholders(Filter):  # type: ignore
    """A Pygments filter for marking up placeholder text.

    You can define the text to highlight with the ``hl_text`` option.
    To add the filter to a Pygments lexer, use the ``add_filter`` method:

    .. code-block:: python

       f = AwesomePlaceholders(hl_text=TEXT)
       lexer.add_filter(AwesomePlaceholders(hl_text=TEXT))

    For more information, see the `Pygments documentation <https://pygments.org/docs/quickstart/>`__.
    """

    def __init__(self: AwesomePlaceholders, **options: str) -> None:
        """Create an instance of the ``AwesomePlaceholders`` filter."""
        Filter.__init__(self, **options)
        placeholders = get_list_opt(options, "hl_text", [])
        self.placeholders_re = re.compile(
            r"|".join([re.escape(x) for x in placeholders if x])
        )

    def filter(
        self: AwesomePlaceholders, _lexer: Any, stream: TokenStream
    ) -> TokenStream:
        """Filter on all tokens."""
        regex = self.placeholders_re
        for ttype, value in stream:
            yield from _replace_placeholders(ttype, value, regex)


class AwesomeHtmlFormatter(HtmlFormatter):  # type: ignore
    """Custom Pygments HTML formatter for highlighting added or removed lines.

    The method is similar to handling the ``hl_lines`` option in the regular HtmlFormatter.
    """

    def _get_line_numbers(
        self: AwesomeHtmlFormatter,
        options: dict[str, Any],
        which: Literal["hl_added", "hl_removed"],
    ) -> set[int]:
        """Get the lines to be added or removed."""
        line_numbers = set()
        for lineno in get_list_opt(options, which, []):
            try:
                line_numbers.add(int(lineno))
            except ValueError:
                pass
        return line_numbers

    def __init__(self: AwesomeHtmlFormatter, **options: Any) -> None:
        """Implement `hl_added` and `hl_removed` options.

        Also set the ``linespans`` and ``wrapcode`` options of the Pygments HTML formatter to ``True``.
        """
        self.added_lines = self._get_line_numbers(options, "hl_added")
        self.removed_lines = self._get_line_numbers(options, "hl_removed")

        # These options aren't compatible with `sphinx.ext.autodoc`
        # options["lineanchors"] = "code"
        options["linespans"] = "line"
        options["wrapcode"] = True

        super().__init__(**options)

    def _highlight_lines(
        self: AwesomeHtmlFormatter, tokensource: TokenStream
    ) -> TokenStream:
        """Highlight added, removed, and emphasized lines.

        In contrast to Pygments, use ``<mark>``, ``<ins>``, and ``<del>`` elements.
        """
        for i, (t, value) in enumerate(tokensource):
            if t != 1:
                yield t, value
            if i + 1 in self.hl_lines:
                yield 1, f"<mark>{value}</mark>"
            elif i + 1 in self.added_lines:
                yield 1, f"<ins>{value}</ins>"
            elif i + 1 in self.removed_lines:
                yield 1, f"<del>{value}</del>"
            else:
                yield 1, value

    def format_unencoded(
        self: AwesomeHtmlFormatter,
        tokensource: TokenStream,
        outfile: Any,
    ) -> None:
        """Overwrite method to handle emphasized, added, and removed lines.

        Unfortunately, the method doesn't extend easily, so I copy it from Pygments.
        """
        source = self._format_lines(tokensource)

        # As a special case, we wrap line numbers before line highlighting
        # so the line numbers get wrapped in the highlighting tag.
        if not self.nowrap and self.linenos == 2:
            source = self._wrap_inlinelinenos(source)

        # This is the only change I made from the original
        if self.hl_lines or self.added_lines or self.removed_lines:
            source = self._highlight_lines(source)

        if not self.nowrap:
            if self.lineanchors:
                source = self._wrap_lineanchors(source)
            if self.linespans:
                source = self._wrap_linespans(source)
            source = self.wrap(source)
            if self.linenos == 1:
                source = self._wrap_tablelinenos(source)
            source = self._wrap_div(source)
            if self.full:
                source = self._wrap_full(source, outfile)

        for _, piece in source:
            outfile.write(piece)


class AwesomePygmentsBridge(PygmentsBridge):  # type: ignore
    """Extend the PygmentsBridge to handle highlighting placeholder text."""

    html_formatter = AwesomeHtmlFormatter

    def get_lexer(
        self: AwesomePygmentsBridge,
        source: str,
        lang: str,
        opts: dict[str, Any] | None = None,
        force: bool = False,
        location: Any = None,
    ) -> Lexer:
        """Extend the ``PygmentsBridge.get_lexer`` method.

        Adds a filter to lexers if the ``hl_text`` option is present.
        """
        lexer = super().get_lexer(source, lang, opts, force, location)
        hl_text = opts.get("hl_text") if opts else None

        if hl_text:
            lexer.add_filter(AwesomePlaceholders(hl_text=hl_text))

        return lexer

    def highlight_block(
        self: AwesomePygmentsBridge,
        source: str,
        lang: str,
        opts: dict[str, Any] | None = None,
        force: bool = False,
        location: Any = None,
        **kwargs: Any,
    ) -> str:
        """Extend the ``PygmentsBridge.highlight_block`` method.

        This method is called when Sphinx transforms the abstract document tree to HTML and encounters code blocks.
        """
        if opts is None:
            opts = {}

        hl_text = get_list_opt(kwargs, "hl_text", [])

        if hl_text:
            opts["hl_text"] = hl_text

        return super().highlight_block(  # type: ignore
            source, lang, opts, force, location, **kwargs
        )

    def get_stylesheet(self: AwesomePygmentsBridge, arg: str | None = None) -> str:
        """Override the ``PygmentsBridge.get_stylesheet`` method.

        This lets you prepend all Pygments classes with a common prefix, such as ``.dark``.
        """
        prefix = ".highlight"
        if arg:
            prefix = f"{arg} .highlight"

        formatter = self.get_formatter()
        if self.dest == "html":
            return formatter.get_style_defs(prefix)  # type: ignore
        else:
            return formatter.get_style_defs() + _LATEX_ADD_STYLES  # type: ignore


def setup(app: Sphinx) -> dict[str, Any]:
    """Set up extension.

    This module is no longer needed as an extension and no code will be run.
    The classes and methods are called from `__init__.py`.
    """
    logger.warning(
        "You no longer have to include the `sphinxawsome_theme.highlighting` extension. This extension will be removed in the next major release."
    )

    return {
        "version": "n/a",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
