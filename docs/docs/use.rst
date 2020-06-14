How to use the theme
====================

.. include:: ../../README.rst
   :start-after: use-start
   :end-before: use-end


How to configure the theme
--------------------------

The theme includes just a few configuration options.
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
   included, but the list of links will not be written on the page itself. This theme
   shows navigation links by default in a navigation menu on the left. Repeating the
   list of links in the main content area is not necessary.

   .. _toctree: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree

   If you don't want to include elements from a ``:hidden:`` toctree directive, set::

      html_theme_options = {"nav_include_hidden": False}


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
