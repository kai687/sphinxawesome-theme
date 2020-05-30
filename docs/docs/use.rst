How to use the theme
====================

.. include:: ../../README.rst
   :start-after: use-start
   :end-before: use-end


How to configure the theme
--------------------------

.. role:: python(code)
   :language: python

.. highlight:: python

The theme includes just a few configuration options. All options can be set as key/value
pairs in the ``html_theme_options`` dictionary in the Sphinx configuration file
``conf.py``.

:python:`nav_include_hidden`
   To include all entries in the navigation menu, add::

      html_theme_options = {"nav_include_hidden": True}

   By default, Sphinx prints a list of links when a toctree_ directive is used to
   include links to other topics. Including the ``:hidden:`` option lets the content be
   included, but the list of links will not be written on the page itself. This can be
   useful, when the navigation links are printed elsewhere, for example in a menu on the
   side.

   .. _toctree: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree

   Setting :python:`"nav_include_hidden": True` includes navigation links from hidden
   ``toctree`` directives into the navigation menu.

   The default setting is :python:`"nav_include_hidden": False` to allow an easier
   transition from other themes.

   .. tip::

      The recommended setting for using the sphinx awesome theme is to include the
      ``:hidden:`` option to all ``toctree`` directives and add the setting::

         html_theme_options = {"nav_include_hidden": True}

:python:`show_nav`
   By default, the navigation links are shown in a navigation menu on the left side. If
   you want to hide the navigation menu, add::

      html_theme_options = {"show_nav": False}

   .. caution::

      If you have multiple pages and don't want to use the side navigation menu, make
      sure to **not** include the ``:hidden:`` option to your ``toctree`` directive,
      otherwise you will not be able to navigate.
