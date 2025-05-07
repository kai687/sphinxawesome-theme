"""Sphinx configuration file."""

from __future__ import annotations

import os
from dataclasses import asdict

from dotenv import load_dotenv
from sphinx.application import Sphinx
from sphinx.util.docfields import Field

from sphinxawesome_theme import ThemeOptions, __version__
from sphinxawesome_theme.postprocess import Icons

load_dotenv()

# -- Project information ---

project = "Awesome Sphinx Theme"
author = "Kai Welke"
copyright = f"{author}."

# -- General configuration ---

extensions = [
    "autoapi.extension",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx_sitemap",
    "sphinx_design",
    "sphinx_docsearch",
    "myst_nb",
]

exclude_patterns = ["public", "includes", "**/includes", "jupyter_execute"]

nitpicky = True

default_role = "literal"

# Global substitutions for reStructuredText files
substitutions = [
    ":tocdepth: 3",
    " ",
    ".. meta::",
    "   :author: kai687",
    "   :keywords: Documentation,Sphinx,Python,Tailwind",
    ".. |rst| replace:: reStructuredText",
    ".. |product| replace:: Awesome Theme",
    ".. |conf| replace:: File: conf.py",
    f".. |current| replace:: {__version__}",
]
rst_prolog = "\n".join(substitutions)

intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

extlinks = {
    "gh": ("https://github.com/kai687/sphinxawesome-theme/blob/main/%s", "%s"),
    "ghdir": ("https://github.com/kai687/sphinxawesome-theme/tree/main/%s", "%s"),
    "sphinxdocs": ("https://www.sphinx-doc.org/en/master/%s", "%s"),
}

autoapi_dirs = ["src"]
autoapi_add_toctree_entry = False

add_module_names = False

# -- Options for HTML output ---

html_title = project
html_theme = "sphinxawesome_theme"
html_last_updated_fmt = ""
html_use_index = False  # Don't create index
html_domain_indices = False  # Don't need module indices
html_copy_source = False  # Don't need sources
html_logo = "assets/auto_awesome.svg"
html_favicon = "assets/favicon-128x128.png"
html_permalinks_icon = Icons.permalinks_icon
html_baseurl = "https://sphinxawesome.xyz/"
html_extra_path = ["robots.txt", "_redirects"]
html_context = {
    "mode": "production",
}

html_sidebars: dict[str, list[str]] = {
    "about": ["sidebar_main_nav_links.html"],
    "changelog/*": ["sidebar_main_nav_links.html"],
}

# if you want to include other pages than docs
templates_path = ["_templates"]
# html_additional_pages = {"about": "about.html"}

# Separate syntax highlighting styles for light and dark mode
# pygments_style = "xcode"
# pygments_style_dark = "github-dark"

# html_static_path = ["_static"]
# html_css_files = ["feedback.css"]
# html_js_files = [("feedback.js", {"defer": "defer"})]

# DocSearch
docsearch_app_id = os.getenv("DOCSEARCH_APP_ID", "")
docsearch_api_key = os.getenv("DOCSEARCH_API_KEY", "")
docsearch_index_name = os.getenv("DOCSEARCH_INDEX_NAME", "")
docsearch_placeholder = "Search these docs"
docsearch_missing_results_url = (
    "https://github.com/kai687/sphinxawesome-theme/issues/new?title=${query}"
)

theme_options = ThemeOptions(
    show_prev_next=True,
    awesome_external_links=True,
    main_nav_links={"Docs": "/index", "About": "/about", "Changelog": "/changelog"},
    extra_header_link_icons={
        "repository on GitHub": {
            "link": "https://github.com/kai687/sphinxawesome-theme",
            "icon": (
                '<svg height="26px" style="margin-top:-2px;display:inline" '
                'viewBox="0 0 45 44" '
                'fill="currentColor" xmlns="http://www.w3.org/2000/svg">'
                '<path fill-rule="evenodd" clip-rule="evenodd" '
                'd="M22.477.927C10.485.927.76 10.65.76 22.647c0 9.596 6.223 17.736 '
                "14.853 20.608 1.087.2 1.483-.47 1.483-1.047 "
                "0-.516-.019-1.881-.03-3.693-6.04 "
                "1.312-7.315-2.912-7.315-2.912-.988-2.51-2.412-3.178-2.412-3.178-1.972-1.346.149-1.32.149-1.32 "  # noqa
                "2.18.154 3.327 2.24 3.327 2.24 1.937 3.318 5.084 2.36 6.321 "
                "1.803.197-1.403.759-2.36 "
                "1.379-2.903-4.823-.548-9.894-2.412-9.894-10.734 "
                "0-2.37.847-4.31 2.236-5.828-.224-.55-.969-2.759.214-5.748 0 0 "
                "1.822-.584 5.972 2.226 "
                "1.732-.482 3.59-.722 5.437-.732 1.845.01 3.703.25 5.437.732 "
                "4.147-2.81 5.967-2.226 "
                "5.967-2.226 1.185 2.99.44 5.198.217 5.748 1.392 1.517 2.232 3.457 "
                "2.232 5.828 0 "
                "8.344-5.078 10.18-9.916 10.717.779.67 1.474 1.996 1.474 4.021 0 "
                "2.904-.027 5.247-.027 "
                "5.96 0 .58.392 1.256 1.493 1.044C37.981 40.375 44.2 32.24 44.2 "
                '22.647c0-11.996-9.726-21.72-21.722-21.72" '
                'fill="currentColor"/></svg>'
            ),
        },
    },
)

html_theme_options = asdict(theme_options)

sitemap_url_scheme = "{link}"


# -- Register a :confval: interpreted text role ----------------------------------
def setup(app: Sphinx) -> None:
    """Register the ``confval`` role and directive.

    This allows to declare theme options as their own object
    for styling and cross-referencing.
    """
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration parameter",
        doc_field_types=[
            Field(
                "default",
                label="default",
                has_arg=True,
                names=("default",),
                bodyrolename="class",
            )
        ],
    )
