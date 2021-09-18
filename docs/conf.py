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
    "sphinxawesome_theme",
    "myst_parser",
    "sphinx_sitemap",
]

myst_enable_extensions = ["colon_fence", "deflist", "replacements", "substitution"]
myst_substitutions = {
    "title": project,
    "description": "Create beautiful and modern documentation websites with Sphinx.",
}

exclude_patterns = ["public"]

nitpicky = True
nitpick_ignore = [
    ("py:class", "sphinx.application.Sphinx"),
    ("py:class", "docutils.nodes.Element"),
]

default_role = "literal"

autodoc_default_flags = ["members"]
autodoc_warningiserror = False

# I keep forgetting how to spell this term
rst_prolog = ".. |rst| replace:: reStructuredText"

intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

extlinks = {
    "gh": ("https://github.com/kai687/sphinxawesome-theme/blob/master/%s", "%s"),
    "ghdir": ("https://github.com/kai687/sphinxawesome-theme/tree/master/%s", "%s"),
}

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
    'viewBox="0 0 24 24">'
    '<path d="M3.9 12c0-1.71 1.39-3.1 '
    "3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 "
    "5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 "
    "13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 "
    "3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 "
    '5-5s-2.24-5-5-5z"/></svg>'
)
html_baseurl = "https://sphinxawesome.xyz/"
html_extra_path = ["robots.txt"]

# if you want to include other pages than docs
# templates_path = ["_templates"]
# html_additional_pages = {"about": "about.html"}

# extra option from the sphinxawesome_theme
html_collapsible_definitions = True

html_awesome_docsearch = True
# These variables are read from `.env` file
# docsearch_api_key = ""
# docsearch_index_name = ""

html_theme_options = {
    "show_scrolltop": True,
    "extra_header_links": {
        "Docs": "/index",
        "About": "/about",
    },
}


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
