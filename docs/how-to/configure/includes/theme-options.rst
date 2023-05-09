.. _sec:theme_options:

Theme options
-------------

To configure the theme, modify the ``html_theme_options`` dictionary in your Sphinx configuration.

``nav_include_hidden``
   Controls whether to include entries from a *hidden*
   :sphinxdocs:`toctree <usage/restructuredtext/directives.html#directive-toctree>`
   directive in the sidebar.

   By default,
   the ``toctree`` directive includes your content *and* generates a list of links in the content area of the page.
   With the ``hidden`` option, the content is still included,
   but no links are printed in the main content area.
   Deprecated: use ``globaltoc_includehidden`` instead (built into Sphinx "basic" theme)

``show_nav``
   Controls whether to render the left sidebar. Deprecated, use ``nosidebar`` instead (built into Sphinx "basic" theme).

``extra_header_links``
   Adds extra links to the header of your documentation.

   The keys of the ``extra_header_links`` dictionary are the link texts.
   The values are absolute URLs.

Theme options reference
-----------------------

.. rst-class:: lead

   The |product| provides a helper class for configuring the :confval:`sphinx:html_theme_options` dictionary.

.. py:module:: sphinxawesome_theme

.. autoclass:: LinkIcon
   :members:

.. autoclass:: ThemeOptions
   :members:

   You can set the following options:
