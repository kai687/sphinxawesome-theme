"""Override code from the default HTML builder related to pygments CSS.

This extension extends the default HTML builder by changing the way
Pygments CSS is handled.

- Add a ``pygments_style_dark`` configuration option.
- Append dark mode styles to the main ``pygments.css`` file,
  scoped to the ``dark`` class set by the theme toggle.

:copyright: Copyright Kai Welke.
:license: MIT, see LICENSE for details.
"""

from __future__ import annotations

import re
from os import path

from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.highlighting import PygmentsBridge

from .highlighting import AwesomePygmentsBridge

# Backgrounds of the code block and (non-special) line numbers belong to the theme,
# so that they follow the page colors regardless of the Pygments style.
_BLOCK_BG = re.compile(r"^\.highlight \{[^}]*\}")
_LINENOS_BG = re.compile(r"^(td\.linenos \.normal|span\.linenos) \{")
_BG = re.compile(r"\s*background(-color)?:[^;}]*;?")


original_init_css_files = StandaloneHTMLBuilder.init_css_files


def _drop_backgrounds(css: str) -> str:
    """Remove theme-owned background declarations from Pygments CSS."""
    lines = []
    for line in css.splitlines():
        if _BLOCK_BG.match(line) or _LINENOS_BG.match(line):
            line = _BG.sub("", line)
        lines.append(line)
    return "\n".join(lines)


class AwesomeHTMLBuilder(StandaloneHTMLBuilder):
    """HTML builder that overrides a few methods related to handling CSS for Pygments."""

    def init_highlighter(self: AwesomeHTMLBuilder) -> None:
        """Initialize Pygments highlighters."""
        # ``pygments_style`` from config
        if self.config.pygments_style is not None:
            style = self.config.pygments_style
        elif self.theme:
            # From the ``pygments_style`` theme setting
            try:
                style = self.theme.pygments_style_default or "none"
            except AttributeError:
                style = self.theme.get_config("theme", "pygments_style", "none")
        else:
            style = "sphinx"

        self.highlighter = AwesomePygmentsBridge("html", style)

        if self.config.pygments_style_dark is not None:
            dark_style = self.config.pygments_style_dark
        elif self.theme:
            try:
                dark_style = self.theme.pygments_style_dark
            except AttributeError:
                dark_style = self.theme.get_config("theme", "pygments_dark_style", None)
        else:
            dark_style = None

        self.dark_highlighter: AwesomePygmentsBridge | PygmentsBridge | None
        if dark_style is not None:
            self.dark_highlighter = AwesomePygmentsBridge("html", dark_style)
        else:
            self.dark_highlighter = None

    def init_css_files(self: AwesomeHTMLBuilder) -> None:
        """Skip Sphinx's separate dark Pygments stylesheet.

        The dark styles are part of ``pygments.css`` and follow the theme toggle,
        so the file ``pygments_dark.css`` doesn't exist.
        """
        dark_highlighter = self.dark_highlighter
        self.dark_highlighter = None
        try:
            original_init_css_files(self)
        finally:
            self.dark_highlighter = dark_highlighter

    def create_pygments_style_file(self: AwesomeHTMLBuilder) -> None:
        """Create CSS file for Pygments."""
        stylesheet = self.highlighter.get_stylesheet()
        if self.dark_highlighter is None and self.config.pygments_style is not None:
            # Keep the selected palette intact across both page modes. Pygments
            # can omit the foreground when it expects black text by default.
            stylesheet = ".highlight { color: #000; }\n" + stylesheet
        else:
            stylesheet = _drop_backgrounds(stylesheet)

        if self.dark_highlighter:
            # Keep the palettes separate without raising selector specificity.
            dark_stylesheet = _drop_backgrounds(self.dark_highlighter.get_stylesheet())
            stylesheet = "\n".join(
                f":where({scope}) {rule}"
                for scope, css in ((":root:not(.dark)", stylesheet), (":root.dark", dark_stylesheet))
                for rule in css.splitlines()
            )

        with open(path.join(self.outdir, "_static", "pygments.css"), "w", encoding="utf-8") as f:
            f.write(stylesheet)
