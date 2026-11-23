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

This documentation uses the ``xcode`` color scheme in light mode
and the ``github-dark`` color scheme in dark mode:

.. code-block:: python
   :caption: |conf|

   pygments_style = "xcode"
   pygments_style_dark = "github-dark"

Both schemes use muted colors, which suit the neutral palette of the theme.
Other Pygments color schemes that you may want to try:

- Light mode: ``default``, ``friendly``, ``vs``
- Dark mode: ``one-dark``, ``nord``, ``night-owl``

Highly saturated color schemes, such as ``monokai`` or ``dracula``, can clash with the rest of the theme.

.. note::

   The theme sets the background color of code blocks,
   so that they match the page in light and dark mode.
   The theme ignores the background color of the Pygments color scheme.
   The theme applies the dark mode scheme when dark mode is on, according to the theme toggle,
   not the operating system setting.
