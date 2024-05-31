Syntax highlighting
-------------------

This theme lets you configure different color themes for syntax highlighting code blocks using these configuration options:

.. code-block:: python
   :caption: |conf|
   :emphasize-text: PYGMENTS_THEME

   # Select theme for both light and dark mode
   pygments_style = "PYGMENTS_THEME"
   # Select a different theme for dark mode
   pygments_style_dark = "PYGMENTS_THEME"

If you only set the :confval:`sphinx:pygments_style` option, the same style will be used in both light and dark modes.
If you specify a ``pygments_style_dark`` option, different colors will be used in light and dark modes.
