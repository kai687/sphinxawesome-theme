.. _sec:theme_options:

.. py:module:: sphinxawesome_theme

Theme options
-------------

To configure the theme, modify the :confval:`sphinx:html_theme_options` dictionary in your Sphinx configuration.
To benefit from code completion and documentation when editing the configuration,
the |product| provides a helper class :py:class:`ThemeOptions` to help with the set up.

To use the ``ThemeOptions`` helper to configure the theme, add the following code:

.. code-block:: python
   :caption: |conf|

   from dataclasses import asdict
   from sphinxawesome_theme import ThemeOptions

   theme_options = ThemeOptions(
      # Add your theme options. For example:
      show_breadcrumbs=True,
      main_nav_links={"About", "/about"},
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

   .. autoclass:: LinkIcon
      :members:
