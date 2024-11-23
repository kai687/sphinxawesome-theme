.. py:module:: sphinxawesome_theme

.. _sec:theme-options:

Theme options
-------------

You can configure the |product| with the :confval:`sphinx:html_theme_options` dictionary.
To benefit from code completion and documentation when editing your Sphinx configuration,
you can use the :py:class:`ThemeOptions` class:

.. code-block:: python
   :caption: |conf|

   from dataclasses import asdict
   from sphinxawesome_theme import ThemeOptions

   theme_options = ThemeOptions(
      # Add your theme options. For example:
      show_breadcrumbs=True,
      main_nav_links={"About": "/about"},
   )

   html_theme_options = asdict(theme_options)

You can still configure the theme using a regular dictionary:

.. code-block:: python
   :caption: |conf|

   html_theme_options = {
      # Add your theme options. For example:
      "show_breadcrumbs": True,
      "main_nav_links": {
         "About": "/about",
      }
   }

.. autoclass:: ThemeOptions()
   :members:
   :exclude-members: extra_header_links, nav_include_hidden, show_nav

.. dropdown:: ``LinkIcon`` reference
   :open:

   .. autoclass:: LinkIcon
      :members:
