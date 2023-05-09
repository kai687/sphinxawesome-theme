"""Add more highlighting options to Pygments.

This extension extends the Sphinx ``code-block``
directive with new options:

- ``:emphasize-added:``: highlight added lines
- ``:emphasize-removed:``: highlight removed lines
- ``:emphasize-text:``: highlight a single word, such as, a placeholder

To achieve this, this extension must make a few larger changes:

1. Provide a custom Sphinx translator to parse the new code block options.
2. Provide a new Sphinx directive to pass along these new options to Pygments.
3. Write a new Pygments HTML formatter and a custom filter to handle these options.

It's entirely possible that there's a simpler way of doing this,
but I haven't found it.

:copyright: Copyright Kai Welke.
:license: MIT, see LICENSE for details.
"""
from __future__ import annotations

import re
from typing import Any, Generator, Pattern, Tuple, Union

from docutils import nodes
from docutils.nodes import Element, Node
from docutils.parsers.rst import directives
from pygments import highlight
from pygments.filter import Filter
from pygments.filters import ErrorToken
from pygments.formatters import HtmlFormatter
from pygments.lexers.shell import BashSessionLexer
from pygments.token import Generic, _TokenType
from pygments.util import get_list_opt
from sphinx.application import Sphinx
from sphinx.directives.code import CodeBlock, container_wrapper, dedent_lines
from sphinx.highlighting import PygmentsBridge
from sphinx.locale import __
from sphinx.util import logging, parselinenos, texescape

from . import __version__

logger = logging.getLogger(__name__)

# type alias
TokenType = Union[_TokenType, int]  # For Python 3.8
TokenStream = Generator[Tuple[TokenType, str], None, None]


def _replace_placeholders(
    ttype: _TokenType, value: str, regex: Pattern[str]
) -> TokenStream:
    """Replace every occurence of `regex` with `Generic.Emph` token."""
    last = 0
    for match in regex.finditer(value):
        start, end = match.start(), match.end()
        if start != last:
            yield ttype, value[last:start]
        yield Generic.Emph, value[start:end]
        last = end
    if last != len(value):
        yield ttype, value[last:]


# Without the comment, `mypy` throws a fit:
# Cannot subclass Filter, is type `Any`


class AwesomePlaceholders(Filter):  # type: ignore[misc]
    """A Pygments filter for marking up placeholder text."""

    def __init__(self: AwesomePlaceholders, **options: str) -> None:
        """Create an instance of the `AwesomePlaceholders` filter."""
        Filter.__init__(self, **options)
        placeholders = get_list_opt(options, "hl_text", [])
        self.placeholders_re = re.compile(
            r"|".join([re.escape(x) for x in placeholders if x])
        )

    def filter(
        self: AwesomePlaceholders, _lexer: Any, stream: TokenStream
    ) -> TokenStream:
        """Filter on all tokens.

        The `lexer` is required by the parent class.
        """
        regex = self.placeholders_re
        for ttype, value in stream:
            yield from _replace_placeholders(ttype, value, regex)


class AwesomeHtmlFormatter(HtmlFormatter):  # type: ignore
    """Custom HTML formatter for Pygments.

    Allow highlighting added or removed lines.
    Similar to emphasizing lines.

    In contrast to Pygments, this formatter returns `<mark>` for higlighted lines.
    """

    def __init__(self: AwesomeHtmlFormatter, **options: Any) -> None:
        """Implement `hl_added` and `hl_removed` options."""
        self.added_lines = set()
        self.removed_lines = set()

        for lineno in get_list_opt(options, "hl_added", []):
            try:
                self.added_lines.add(int(lineno))
            except ValueError:
                pass

        for lineno in get_list_opt(options, "hl_removed", []):
            try:
                self.removed_lines.add(int(lineno))
            except ValueError:
                pass

        # These options aren't compatible with `sphinx.ext.autodoc`
        # options["lineanchors"] = "code"
        options["linespans"] = "line"
        options["wrapcode"] = True

        super().__init__(**options)

    def _highlight_lines(
        self: AwesomeHtmlFormatter, tokensource: TokenStream
    ) -> TokenStream:
        """Highlight added, removed, and emphasized lines.

        In contrast to Pygments, use `<mark>`, `<ins>`, and `<del>` elements.
        """
        for i, (t, value) in enumerate(tokensource):
            if t != 1:
                yield t, value
            if i + 1 in self.hl_lines:
                yield 1, "<mark>%s</mark>" % value
            elif i + 1 in self.added_lines:
                yield 1, "<ins>%s</ins>" % value
            elif i + 1 in self.removed_lines:
                yield 1, "<del>%s</del>" % value
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


def _get_parsed_line_numbers(linespec: str, nlines: int, location: str) -> list[int]:
    """Get the parsed line numbers for the `emphasize-*` options."""
    line_numbers = parselinenos(linespec, nlines)
    if any(i >= nlines for i in line_numbers):
        logger.warning(
            __("line number spec is out of range(1-%d): %r") % (nlines, linespec),
            location=location,
        )
    return [x + 1 for x in line_numbers if x < nlines]


class AwesomeCodeBlock(CodeBlock):
    """Add options to highlight added and removed lines to `code-block` directives."""

    new_options = {
        "emphasize-added": directives.unchanged_required,
        "emphasize-removed": directives.unchanged_required,
        "emphasize-text": directives.unchanged_required,
    }

    option_spec = CodeBlock.option_spec
    option_spec.update(new_options)

    def run(self: AwesomeCodeBlock) -> list[Node]:  # noqa
        """Overwrite method from Sphinx.

        Add ability to highlight added and removed lines.
        This passes the options to the highlighter.
        You need a custom pygments formatter.

        Unfortunately, the original method doesn't lend itself to being extended,
        so I had to copy it.
        """
        document = self.state.document
        code = "\n".join(self.content)
        location = self.state_machine.get_source_and_line(self.lineno)
        nlines = len(self.content)

        hl_lines = hl_added = hl_removed = None
        linespec = self.options.get("emphasize-lines")
        if linespec:
            try:
                hl_lines = _get_parsed_line_numbers(linespec, nlines, location)
            except ValueError as err:
                return [document.reporter.warning(err, line=self.lineno)]

        linespec = self.options.get("emphasize-added")
        if linespec:
            try:
                hl_added = _get_parsed_line_numbers(linespec, nlines, location)
            except ValueError as err:
                return [document.reporter.warning(err, line=self.lineno)]

        linespec = self.options.get("emphasize-removed")
        if linespec:
            try:
                hl_removed = _get_parsed_line_numbers(linespec, nlines, location)
            except ValueError as err:
                return [document.reporter.warning(err, line=self.lineno)]

        if "dedent" in self.options:
            lines = code.splitlines(True)
            lines = dedent_lines(lines, self.options["dedent"], location=location)
            code = "".join(lines)

        literal: Element = nodes.literal_block(code, code)
        if "linenos" in self.options or "lineno-start" in self.options:
            literal["linenos"] = True
        literal["classes"] += self.options.get("class", [])
        literal["force"] = "force" in self.options
        if self.arguments:
            # highlight language specified
            literal["language"] = self.arguments[0]
        else:
            # no highlight language specified.  Then this directive refers the current
            # highlight setting via ``highlight`` directive or ``highlight_language``
            # configuration.
            literal["language"] = self.env.temp_data.get(
                "highlight_language", self.config.highlight_language
            )
        extra_args = literal["highlight_args"] = {}
        if hl_lines is not None:
            extra_args["hl_lines"] = hl_lines
        if hl_added is not None:
            extra_args["hl_added"] = hl_added
        if hl_removed is not None:
            extra_args["hl_removed"] = hl_removed
        if "lineno-start" in self.options:
            extra_args["linenostart"] = self.options["lineno-start"]
        if "emphasize-text" in self.options:
            extra_args["hl_text"] = self.options["emphasize-text"]

        self.set_source_info(literal)

        caption = self.options.get("caption")
        if caption:
            try:
                literal = container_wrapper(self, literal, caption)
            except ValueError as exc:
                return [document.reporter.warning(exc, line=self.lineno)]

        # literal will be note_implicit_target that is linked from caption and numref.
        # when options['name'] is provided, it should be primary ID.
        self.add_name(literal)

        return [literal]


class AwesomePygmentsBridge(PygmentsBridge):
    """Class for monkeypatching."""

    def highlight_block(
        self: PygmentsBridge,
        source: str,
        lang: str,
        opts: dict[str, Any] | None = None,
        force: bool = False,
        location: Any = None,
        **kwargs: Any,
    ) -> str:
        """Repeat this method."""
        if not isinstance(source, str):
            source = source.decode()  # type: ignore[unreachable]

        lexer = self.get_lexer(source, lang, opts, force, location)
        hl_text = get_list_opt(kwargs, "hl_text", [])
        if hl_text:
            lexer.add_filter(AwesomePlaceholders(hl_text=hl_text))

        # highlight via Pygments
        formatter = self.get_formatter(**kwargs)
        try:
            hlsource: str = highlight(source, lexer, formatter)
        except ErrorToken:
            # this is most probably not the selected language,
            # so let it pass unhighlighted
            if lang == "default":
                pass  # automatic highlighting failed.
            else:
                logger.warning(
                    __('Could not lex literal_block as "%s". ' "Highlighting skipped."),
                    lang,
                    type="misc",
                    subtype="highlighting_failure",
                    location=location,
                )
            lexer = self.get_lexer(source, "none", opts, force, location)
            hlsource = highlight(source, lexer, formatter)

        if self.dest == "html":
            return hlsource
        else:
            # MEMO: this is done to escape Unicode chars with non-Unicode engines
            return texescape.hlescape(hlsource, self.latex_engine)


def setup(app: Sphinx) -> dict[str, Any]:
    """Set up this internal extension."""
    PygmentsBridge.html_formatter = AwesomeHtmlFormatter
    PygmentsBridge.highlight_block = AwesomePygmentsBridge.highlight_block  # type: ignore[method-assign]  # noqa
    directives.register_directive("code-block", AwesomeCodeBlock)

    # Allow using `terminal` in addition to `shell-session` and `console`
    # for interactive command-line sessions
    app.add_lexer("terminal", BashSessionLexer)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
