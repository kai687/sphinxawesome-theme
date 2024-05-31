"""Extend Sphinx's code-block directive.

New options:

- ``:emphasize-added:``: highlight added lines
- ``:emphasize-removed:``: highlight removed lines
- ``:emphasize-text:``: highlight a single word, such as, a placeholder

:copyright: Copyright Kai Welke.
:license: MIT, see LICENSE for details.
"""

from __future__ import annotations

from typing import Any, Literal

from docutils import nodes
from docutils.nodes import Node
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.directives.code import CodeBlock
from sphinx.locale import __
from sphinx.util import logging, parselinenos

logger = logging.getLogger(__name__)


class AwesomeCodeBlock(CodeBlock):  # type: ignore
    """An extension of the Sphinx ``code-block`` directive to handle additional options.

    - ``:emphasize-added:`` highlight added lines
    - ``:emphasize-removed:`` highlight removed lines
    - ``:emphasize-text:`` highlight placeholder text

    The job of the directive is to set the correct options for the ``literal_block`` node,
    which represents a code block in the parsed reStructuredText tree.
    When transforming the abstract tree to HTML,
    Sphinx passes these options to the ``highlight_block`` method,
    which is a wrapper around Pygments' ``highlight`` method.
    Handling these options is then a job of the ``AwesomePygmentsBridge``.
    """

    new_options = {
        "emphasize-added": directives.unchanged_required,
        "emphasize-removed": directives.unchanged_required,
        "emphasize-text": directives.unchanged_required,
    }

    option_spec = CodeBlock.option_spec  # type: ignore[misc]
    option_spec.update(new_options)

    def _get_line_numbers(
        self: AwesomeCodeBlock, option: Literal["emphasize-added", "emphasize-removed"]
    ) -> list[int] | None:
        """Parse the line numbers for the ``:emphasize-added:`` and ``:emphasize-removed:`` options."""
        document = self.state.document
        location = self.state_machine.get_source_and_line(self.lineno)
        nlines = len(self.content)
        linespec = self.options.get(option)

        if not linespec:
            return None

        try:
            line_numbers = parselinenos(linespec, nlines)
            if any(i >= nlines for i in line_numbers):
                logger.warning(
                    __("line number spec is out of range(1-%d): %r")
                    % (nlines, linespec),
                    location=location,
                )
            return [i + 1 for i in line_numbers if i < nlines]
        except ValueError as err:
            return [document.reporter.warning(err, line=self.lineno)]

    def _extra_args(
        self: AwesomeCodeBlock,
        node: Node,
        hl_added: list[int] | None,
        hl_removed: list[int] | None,
    ) -> None:
        """Set extra attributes for line highlighting."""
        extra_args = node.get("highlight_args", {})  # type: ignore[attr-defined]

        if hl_added is not None:
            extra_args["hl_added"] = hl_added
        if hl_removed is not None:
            extra_args["hl_removed"] = hl_removed
        if "emphasize-text" in self.options:
            extra_args["hl_text"] = self.options["emphasize-text"]

    def run(self: AwesomeCodeBlock) -> list[Node]:
        """Handle parsing extra options for highlighting."""
        literal_nodes: list[Node] = super().run()

        hl_added = self._get_line_numbers("emphasize-added")
        hl_removed = self._get_line_numbers("emphasize-removed")

        for node in literal_nodes:
            # Code blocks with caption [container > (caption + literal_block)]
            if isinstance(node, nodes.container):
                for nnode in node.children:
                    if isinstance(nnode, nodes.literal_block):
                        self._extra_args(nnode, hl_added, hl_removed)
            # Code blocks without caption [literal_block]
            if isinstance(node, nodes.literal_block):
                self._extra_args(node, hl_added, hl_removed)

        return literal_nodes


def setup(app: Sphinx) -> dict[str, Any]:
    """Set up extension."""
    logger.warning(
        "You no longer have to include `sphinxawesome_theme.highlighting` in your extensions."
        "This extension will be removed in the next major version."
    )

    return {
        "version": "n/a",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
