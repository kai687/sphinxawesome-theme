"""Check for deprecated options.

This extension checks if you're using a deprecated option from the
sphinxawesome_theme from a version < 5.0.

Theme options in the ``html_theme_options`` dictionary are handled automatically.
Regular configuration options however need to be checked separately,
because the HTML theme is loaded _after_ the configuration is handled,
and extensions are already processed.

To load this extension, add:

.. code-block:: python
   :caption: |conf|

   extensions += ["sphinxawesome_theme.deprecated"]

:copyright: Kai Welke.
:license: MIT, see LICENSE for details
"""

from __future__ import annotations

from typing import Any

from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util import logging

from . import __version__

logger = logging.getLogger(__name__)


def check_deprecated(app: Sphinx, config: Config) -> None:  # noqa: C901
    """Check the Sphinx configuration for the deprecated options and migrate them automatically if possible."""
    raw = config._raw_config
    found_deprecated = False

    if "html_collapsible_definitions" in raw:
        logger.warning(
            "`html_collapsible_definitions` is deprecated. "
            "Use the `sphinx-design` extension instead."
        )
        found_deprecated = True

    if "html_awesome_headerlinks" in raw:
        logger.warning(
            "`html_awesome_headerlinks` is deprecated. "
            "Use `html_theme_options = {'awesome_headerlinks: True '} instead."
        )
        config.html_theme_options["awesome_headerlinks"] = raw[
            "html_awesome_headerlinks"
        ]
        found_deprecated = True

    if "html_awesome_external_links" in raw:
        logger.warning(
            "`html_awesome_external_links` is deprecated. "
            "Use `html_theme_options = {'awesome_external_links: True '} instead."
        )
        config.html_theme_options["awesome_external_links"] = raw[
            "html_awesome_external_links"
        ]
        found_deprecated = True

    # Since this won't have any effect, it shouldn't be a warning.
    if "html_awesome_code_headers" in raw:
        logger.info(
            "`html_awesome_code_headers` is deprecated. "
            "You can remove it from your Sphinx configuration."
        )
        found_deprecated = True

    if "html_awesome_docsearch" in raw:
        logger.warning(
            "`html_awesome_docsearch` is deprecated. "
            "Use the `sphinx-docsearch` extension instead."
        )
        found_deprecated = True

    if found_deprecated is False:
        logger.info(
            "No deprecated options found. You can remove the `sphinxawesome_theme.deprecated` extension."
        )


def setup(app: Sphinx) -> dict[str, Any]:
    """Register the extension."""
    if "sphinxawesome_theme" in app.config.extensions:
        logger.warning(
            "Including `sphinxawesome_theme` in your `extensions` is deprecated. "
            'Setting `html_theme = "sphinxawesome_theme"` is enough. '
        )

    if "sphinxawesome_theme.highlighting" in app.config.extensions:
        logger.warning(
            "You don't need to include the `sphinxawesome_theme.highlighting` extension anymore."
        )

    # If we don't register these options, Sphinx ignores them when evaluating the `conf.py` file.
    app.add_config_value(
        name="html_collapsible_definitions", default=False, rebuild="html", types=(bool)
    )
    app.add_config_value(
        name="html_awesome_external_links", default=False, rebuild="html", types=(bool)
    )
    app.add_config_value(
        name="html_awesome_docsearch", default=False, rebuild="html", types=(bool)
    )
    app.add_config_value(
        name="docsearch_config", default={}, rebuild="html", types=(dict)
    )
    app.add_config_value(
        name="html_awesome_headerlinks", default=True, rebuild="html", types=(str)
    )
    app.add_config_value(
        name="html_awesome_code_headers", default=True, rebuild="html", types=(str)
    )

    app.connect("config-inited", check_deprecated)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
