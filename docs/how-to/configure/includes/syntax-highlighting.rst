Syntax highlighting
-------------------

You can use any Pygments color scheme for syntax highlighting in code blocks.
To use different color schemes for light mode and dark mode,
set the :confval:`sphinx:pygments_style` parameter and the ``pygments_style_dark`` parameter.
To use the same color scheme in both modes,
set only the ``pygments_style`` parameter:

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

Both schemes use muted colors. These colors suit the neutral palette of the theme.
You can also try these Pygments color schemes:

- Light mode: ``default``, ``friendly``, ``vs``
- Dark mode: ``one-dark``, ``nord``, ``night-owl``

Do not use highly saturated color schemes, such as ``monokai`` or ``dracula``. They can clash with the rest of the theme.

.. note::

   The theme sets the background color of code blocks
   to match the page in light mode and in dark mode.
   The theme ignores the background color of the Pygments color scheme.
   The theme uses the dark mode scheme when the theme toggle is set to dark mode.
   It does not use the operating system setting.
