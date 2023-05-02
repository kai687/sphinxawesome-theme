"""Sphinx configuration file."""
import sys
from pathlib import Path

from sphinx.application import Sphinx
from sphinx.util.docfields import Field

# Add path to local extension
this_dir = Path(__file__).parent
ext_dir = (this_dir / ".." / "src").resolve()
sys.path.append(str(ext_dir.absolute()))

# -- Project information -----------------------------------------------------

project = "Awesome Sphinx Theme"
author = "Kai Welke"
copyright = f"{author}."

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.viewcode",
    "sphinxawesome_theme",
    "sphinx_sitemap",
    "sphinx_design",
]

exclude_patterns = ["public", "includes", "**/includes"]

nitpicky = True
nitpick_ignore = [
    ("py:class", "sphinx.application.Sphinx"),
    ("py:class", "docutils.nodes.Element"),
]

default_role = "literal"

# Global substitutions for reStructuredText files
rst_prolog = """
.. |rst| replace:: reStructuredText
.. |product| replace:: Awesome Theme
"""

intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

extlinks = {
    "gh": ("https://github.com/kai687/sphinxawesome-theme/blob/master/%s", "%s"),
    "ghdir": ("https://github.com/kai687/sphinxawesome-theme/tree/master/%s", "%s"),
    "sphinxdocs": ("https://www.sphinx-doc.org/en/master/%s", "%s"),
}

linkcheck_ignore = [
    # GitHub anchors are dynamically created and difficult to check
    # See https://github.com/sphinx-doc/sphinx/issues/9016
    "https://github.com/cjolowicz/nox-poetry/#installation",
    "https://github.com/wntrblm/nox/#installation",
]

# -- Options for HTML output -------------------------------------------------

html_title = project
html_theme = "sphinxawesome_theme"
html_theme_path = ["../src"]
html_last_updated_fmt = ""
html_use_index = False  # Don't create index
html_domain_indices = False  # Don't need module indices
html_copy_source = False  # Don't need sources
html_logo = "assets/auto_awesome.svg"
html_favicon = "assets/favicon-128x128.png"
html_permalinks_icon = (
    '<svg xmlns="http://www.w3.org/2000/svg" '
    'height="1em" width="1em" '
    'viewBox="0 0 24 24">'
    '<path d="M3.9 12c0-1.71 1.39-3.1 '
    "3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 "
    "5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 "
    "13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 "
    "3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 "
    '5-5s-2.24-5-5-5z"/></svg>'
)
html_baseurl = "https://sphinxawesome.xyz/"
html_extra_path = ["robots.txt", "_redirects"]
html_context = {
    "mode": "production",
    "feedback_url": "https://github.com/kai687/sphinxawesome-theme/issues/new?title=Feedback",
}

# if you want to include other pages than docs
templates_path = ["_templates"]
# html_additional_pages = {"about": "about.html"}

html_static_path = ["_static"]
html_css_files = ["feedback.css"]
html_js_files = ["feedback.js"]

# extra options from the sphinxawesome_theme
html_awesome_docsearch = True
html_awesome_external_links = False
html_awesome_postprocessing = True
html_awesome_code_headers = False

# The Algolia credentials are added from an `.env` file
docsearch_config = {
    "placeholder": "Search these docs",
    "missing_results_url": "https://github.com/kai687/sphinxawesome-theme/issues/new?title=${query}",
}

html_theme_options = {
    "show_scrolltop": True,
    "show_prev_next": True,
    "main_nav_links": {
        "Docs": "/index",
        "About": "/about",
        "Changelog": "/changelog",
    },
    "extra_header_link_icons": {
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
}

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
