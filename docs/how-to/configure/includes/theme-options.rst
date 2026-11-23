.. py:module:: sphinxawesome_theme

.. _sec:theme-options:

Theme options
-------------

Use the :confval:`sphinx:html_theme_options` dictionary to configure the |product|.
For code completion and documentation in your editor,
use the :py:class:`ThemeOptions` class:

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

You can also use a regular dictionary:

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

.. dropdown:: ``LinkIcon`` reference
   :open:

   .. autoclass:: LinkIcon
      :members:
