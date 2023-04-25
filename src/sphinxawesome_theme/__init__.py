"""The Sphinx awesome theme as a Python package.

:copyright: Copyright Kai Welke.
:license: MIT, see LICENSE_ for details

.. _LICENSE: https://github.com/kai687/sphinxawesome-theme/blob/master/LICENSE
"""

from importlib.metadata import PackageNotFoundError, version
from os import path
from typing import Any, Dict

from sphinx.application import Sphinx
from sphinx.config import Config
from sphinxcontrib.serializinghtml import JSONHTMLBuilder

from . import jsonimpl

try:
    # obtain version from `pyproject.toml` via `importlib.metadata.version()`
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"


def post_config_setup(app: Sphinx, config: Config) -> None:
    """Set up extensions if configuration is ready."""
    if config.html_awesome_highlighting:
        app.setup_extension("sphinxawesome_theme.highlighting")

    if config.html_awesome_external_links:
        app.setup_extension("sphinxawesome_theme.html_translator")

    # The awesome code headers are handled in `postprocessing`
    if config.html_awesome_postprocessing or config.html_awesome_code_headers:
        app.setup_extension("sphinxawesome_theme.postprocess")

    if config.html_awesome_docsearch:
        app.setup_extension("sphinxawesome_theme.docsearch")

    # Add the CSS overrides if we're using the `sphinx-design` extension
    if "sphinx_design" in app.extensions:
        app.add_css_file("awesome-sphinx-design.css", priority=900)


def setup(app: "Sphinx") -> Dict[str, Any]:
    """Register the theme and its extensions wih Sphinx."""
    app.add_html_theme(
        name="sphinxawesome_theme", theme_path=path.abspath(path.dirname(__file__))
    )
    app.add_config_value(
        name="html_awesome_postprocessing", default=True, rebuild="html", types=(bool)
    )
    app.add_config_value(
        name="html_awesome_highlighting", default=True, rebuild="html", types=(bool)
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

    app.setup_extension("sphinxawesome_theme.jinja_functions")
    app.connect("config-inited", post_config_setup)

    JSONHTMLBuilder.out_suffix = ".json"
    JSONHTMLBuilder.implementation = jsonimpl
    JSONHTMLBuilder.indexer_format = jsonimpl

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
