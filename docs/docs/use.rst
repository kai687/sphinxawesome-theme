How to use the theme
====================

.. include:: ../../README.rst
   :start-after: use-start
   :end-before: use-end

The theme activates the extension ``sphinxawesome.sampdirective``
and other usability improvements automatically
if the theme is installed and loaded as a python package.
If the theme is installed locally, see :ref:`How to use a local version of the theme`.

How to configure the theme
--------------------------

All options can be set as key/value pairs
in the ``html_theme_options`` dictionary
in the Sphinx configuration file :file:`conf.py`::

   html_theme_options = {
       "nav_include_hidden": True,
       "show_nav": True,
       "show_breadcrumbs": True,
       "breadcrumbs_separator": "/"
   }

.. rubric:: Available options

``nav_include_hidden`` (default: ``True``)
   By default, Sphinx prints a list of links when a toctree_ directive is used to
   include links to other topics. Including the ``:hidden:`` option lets the content be
   included, but the list of links isn't written on the page itself. This theme
   shows navigation links by default in a navigation menu on the left. Repeating the
   list of links in the main content area isn't necessary.

   .. _toctree: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree

   If you don't want to include elements from a ``:hidden:`` toctree directive, set::

      html_theme_options = {"nav_include_hidden": False}

   It's recommended to either provide a caption to the toctree directive, or inserting
   a headline before it when not using the ``:hidden:`` option. For example::

      .. toctree::
         :caption: Contents

``show_nav`` (default: ``True``)
   By default, the navigation links are shown in a navigation menu on the left side. If
   you want to hide the navigation menu, add::

      html_theme_options = {"show_nav": False}

``show_breadcrumbs`` (default: ``True``)
   By default, so-called “breadcrumbs” navigation links are shown at the top of the
   content area to show the position of this document relative to the top-level. If you
   want to hide the breadcrumbs navigation links, add::

      html_theme_options = {"show_breadcrumbs": False}

``breadcrumbs_separator`` (default: ``/``)
   If you want to select a different separator for the breadcrumbs navigation links,
   set::

      html_theme_options = {"breadcrumbs_separator": "{Char}"}

   Replace ``{Char}`` with a character or HTML entity of your choice.


How to use a local version of the theme
---------------------------------------

If you didn't install the theme as a Python package,
but :ref:`installed it locally <Installing the theme locally>`,
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
:ref:`clone the repository <Installing the theme locally>`.

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
