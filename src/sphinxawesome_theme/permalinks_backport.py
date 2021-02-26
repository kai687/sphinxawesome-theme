"""Backport of the new permalink options for Sphinx versions <3.5.

For Sphinx versions <3.5, the option ``html_add_permalinks`` is used.
This is replaced by ``html_permalinks`` and ``html_permalinks_icon``.

This theme uses the new options. In order to make this theme work with
older versions of Sphinx, this extension implements the new configuration
options.

:copyright: Kai Welke
:license: MIT, see LICENSE for details
"""

from typing import Any, Dict, List

from sphinx import version_info
from sphinx.application import Sphinx
from sphinx.config import Config

from . import __version__


def needs_backport(version_info: List[Any]) -> bool:
    """Return true for Sphinx versions <3.5."""
    major, minor, *rest = version_info

    if major < 4 and minor < 5:
        return True

    return False


def migrate_html_add_permalinks(app: Sphinx, config: Config) -> None:
    """Migrate html_add_permalinks to html_permalinks.

    This is a simplification from the function of the same name,
    that's implemented in Sphinx 3.5. Since we deliver our own
    icon, we don't use `html_permalinks_icon`.

    Any non-false value for `html_add_permalinks` will set `html_permalinks` to True.
    """
    if config.html_add_permalinks and config.html_add_permalinks is False:
        config.html_permalinks = False


def setup(app: Sphinx) -> Dict[str, Any]:
    """Setup as extension."""
    if needs_backport(version_info):
        app.add_config_value("html_permalinks", True, "html")
        app.connect("config-inited", migrate_html_add_permalinks, priority=800)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
