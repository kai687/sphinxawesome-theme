How to use the theme
====================

.. include:: ../../README.rst
   :start-after: use-start
   :end-before: use-end

If you install and load the theme as a Python package,
the Sphinx extension ``sphinxawesome.sampdirective``
is installed and used automatically.
If the theme is loaded from a local directory,
see :ref:`How to use a local version of the theme`.

How to configure the theme
--------------------------

The following options can be set as key/value pairs
in the ``html_theme_options`` dictionary
in the Sphinx configuration file :file:`conf.py`.

.. code-block:: python
   :caption: conf.py

   html_theme_options = {
       "nav_include_hidden": True,
       "show_nav": True,
       "show_breadcrumbs": True,
       "breadcrumbs_separator": "/"
   }

.. rubric:: Theme options

.. confval:: nav_include_hidden

   By default, the toctree_ directive both includes the content as well as prints
   a list of links in the content area, where the directive is included.
   A ``toctree`` directive with the ``:hidden:`` option includes the content,
   but doesn't print the list of links in the content area. This can be useful
   if navigation links are elsewhere on the page, and printing the same list of links
   in the content area would be redundant.

   .. _toctree: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree

   If you don't want to include elements from a ``:hidden:`` toctree directive in the
   navigation menu on the left, set:

   .. code-block:: python
      :caption: conf.py

      html_theme_options = {"nav_include_hidden": False}

   When using the ``toctree`` directive without the ``:hidden:`` option, insert a
   headline or provide a caption with the ``:caption:`` option for the list of links
   in the content area. For example:

   .. code-block:: rst

      .. toctree::
         :caption: Contents

.. confval:: show_nav

   By default, the navigation links are shown in a navigation menu on the left side. If
   you want to hide the navigation menu completely, add:

   .. code-block:: python
      :caption: conf.py

      html_theme_options = {"show_nav": False}

.. confval:: show_breadcrumbs

   By default, “breadcrumbs_” navigation links are shown at the top of the
   content area to show the position of this document relative to the top-level. If you
   want to hide the breadcrumbs navigation links, add:

   .. code-block:: python
      :caption: conf.py

      html_theme_options = {"show_breadcrumbs": False}

   .. _breadcrumbs: https://en.wikipedia.org/wiki/Breadcrumb_navigation

.. confval:: breadcrumbs_separator

   If you want to select a different separator for the breadcrumbs navigation links,
   set:

   .. samp::

      html_theme_options = \{"breadcrumbs_separator": "{CHAR}"\}

   Replace :samp:`{CHAR}` with a character or HTML entity of your choice.

.. rubric:: Extension options

This theme also enables a few internal extensions that enhance the user experience.
The following additional configuration value is set at the top level in the Sphinx
configuration file :file`conf.py`:

.. confval:: html_collapsible_definitions

   Set the ``html_collapsible_definitions`` option to ``True`` to enable collapsible
   object definitions, such as command line options, classes, methods, and so on.

   .. code-block:: python
      :caption: conf.py

      html_collapsible_definitions = True

How to use a local version of the theme
---------------------------------------

If you didn't install the theme as a Python package,
you can :ref:`install it locally <Creating a local copy of the theme>`

For example, you have a project structure like this:

.. code-block:: console
   :emphasize-lines: 3

   ./
   ├conf.py
   ├index.rst
   └sphinxawesome-theme/

Add this directory to the Sphinx configuration in :file:`conf.py`:

.. code-block:: python
   :caption: conf.py

   import os
   import sys

   sys.path.append(os.path.abspath("sphinxawesome-theme/src"))

To prevent Sphinx from looking for source files in this directory,
add it to the ``exclude_patterns`` list:

.. code-block:: python
   :caption: conf.py

   exclude_patterns = ["sphinxawesome-theme", "..."]

Next, add the ``sphinxawesome_theme`` as extension and ``html_theme``:

.. code-block:: python
   :caption: conf.py

   extensions = ["sphinxawesome_theme", "..."]
   html_theme = "sphinxawesome_theme"

.. note::

   These additional steps are necessary
   in order to create a fully functional local version of the theme.
   This is because locally installed Sphinx themes
   are loaded differently than themes installed as Python packages.
