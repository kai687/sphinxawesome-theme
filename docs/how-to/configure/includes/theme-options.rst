.. _sec:theme_options:

Theme options
-------------

To configure the theme, modify the ``html_theme_options`` dictionary in your Sphinx configuration.

.. code-block:: python
   :caption: File: conf.py

   # Default values
   html_theme_options = {
       "nav_include_hidden": True,
       "show_nav": True,
       "show_breadcrumbs": True,
       "breadcrumbs_separator": "/",
       "show_prev_next": False,
       "show_scrolltop": False,
       "extra_headerlinks": False,
   }

``nav_include_hidden``
   Controls whether to include entries from a *hidden*
   :sphinxdocs:`toctree <usage/restructuredtext/directives.html#directive-toctree>`
   directive in the sidebar.

   By default,
   the ``toctree`` directive includes your content *and* generates a list of links in the content area of the page.
   With the ``hidden`` option, the content is still included,
   but no links are printed in the main content area.

``show_nav``
   Controls whether to render the left sidebar.

``show_breadcrumbs``
   Controls whether to include `breadcrumbs <https://en.wikipedia.org/wiki/Breadcrumb_navigation>`_ links at the top of each page.

``breadcrumbs_separator``
   The separator for the breadcrumbs links.

``show_prev_next``
   Controls whether to show links to the previous and next pages in the hierarchy.

``show_scrolltop``
   Controls whether to show a button that scrolls to the top of the page when clicked.

``extra_header_links``
   Adds extra links to the header of your documentation.

   The keys of the ``extra_header_links`` dictionary are the link texts.
   The values are absolute URLs.
