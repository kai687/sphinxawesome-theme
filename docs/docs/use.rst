How to use the theme
====================

.. include:: ../../README.rst
   :start-after: use-start
   :end-before: use-end

The theme activates the extension ``sphinxawesome.sampdirective``
and other usability improvements automatically
if the theme is installed and loaded as a python package.
If the theme is installed locally,
see :ref:`How to use a local version of the theme`.

How to configure the theme
--------------------------

All options can be set as key/value pairs
in the ``html_theme_options`` dictionary
in the Sphinx configuration file :file:`conf.py`.
The available options and their default values for this theme are::

   html_theme_options = {
       "nav_include_hidden": True,
       "show_nav": True,
       "show_breadcrumbs": True,
       "breadcrumbs_separator": "/"
   }

.. rubric:: Available options

.. confval:: nav_include_hidden

   By default, the toctree_ directive both includes the content as well as prints
   a list of links in the content area, where the directive is included.
   A ``toctree`` directive with the ``:hidden:`` option includes the content,
   but doesn't print the list of links in the content area. This can be useful
   if navigation links are elsewhere on the page, and printing the same list of links
   in the content area would be redundant.

   .. _toctree: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree

   If you don't want to include elements from a ``:hidden:`` toctree directive in the
   navigation menu on the left, set::

      html_theme_options = {"nav_include_hidden": False}

   When using the ``toctree`` directive without the ``:hidden:`` option, insert a
   headline or provide a caption with the ``:caption:`` option for the list of links
   in the content area. For example::

      .. toctree::
         :caption: Contents

.. confval:: show_nav

   By default, the navigation links are shown in a navigation menu on the left side. If
   you want to hide the navigation menu completely, add::

      html_theme_options = {"show_nav": False}

.. confval:: show_breadcrumbs

   By default, “breadcrumbs_” navigation links are shown at the top of the
   content area to show the position of this document relative to the top-level. If you
   want to hide the breadcrumbs navigation links, add::

      html_theme_options = {"show_breadcrumbs": False}

   .. _breadcrumbs: https://en.wikipedia.org/wiki/Breadcrumb_navigation

.. confval:: breadcrumbs_separator

   If you want to select a different separator for the breadcrumbs navigation links,
   set::

      html_theme_options = {"breadcrumbs_separator": "{Char}"}

   Replace ``{Char}`` with a character or HTML entity of your choice.


How to use a local version of the theme
---------------------------------------

If you didn't install the theme as a Python package,
but installed it locally Installing the theme locally,
place it inside a directory
:dir:`_ext`, or :dir:`_themes`
to keep the project tidy.

For example, if you have a project structure like this:

.. code-block:: console

   ./
   ├conf.py
   ├index.rst
   └_themes/

Change to the :dir:`_themes` directory and
clone the repository Installing the theme locally.

Next, add this directory to the Sphinx configuration in :file:`conf.py`::

   html_theme = "sphinxawesome_theme"
   html_theme_path = ["_themes"]

**Recommended:** Add the theme as extension as well,
to enable the ``samp`` directive extensions and other
usability improvements.

Add these modifications to your Sphinx configuration :file:`conf.py`:

#. Add the path to the :dir:`_themes/` directory::

      from pathlib import Path
      import sys

      this_dir = Path(__file__).parent
      ext_dir = (this_dir / "_themes").resolve()
      sys.path.append(str(ext_dir.absolute()))

#. Add the theme to the list of extensions::

      extensions = ["...", "sphinxawesome_theme"]

.. note::

   These additional steps are necessary, because local Sphinx themes
   get loaded differently than themes installed as Python packages.
   For locally installed themes, no Python code is executed. Therefore,
   no additional extensions can be loaded without these extra steps.
