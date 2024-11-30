Syntax highlighting
-------------------

You can choose any Pygments color scheme for syntax highlighting in code blocks.
To use different color schemes for both light and dark modes,
set both the :confval:`sphinx:pygments_style` and ``pygments_style_dark`` parameters.
To use the same color scheme in light and dark mode,
only set the ``pygments_style`` parameter:

.. code-block:: python
   :caption: |conf|
   :emphasize-text: PYGMENTS_THEME

   # Select a color scheme for light mode
   pygments_style = "PYGMENTS_THEME"
   # Select a different color scheme for dark mode
   pygments_style_dark = "PYGMENTS_THEME"
