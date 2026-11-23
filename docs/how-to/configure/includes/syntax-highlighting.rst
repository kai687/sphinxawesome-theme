Syntax highlighting
-------------------

You can use any Pygments color scheme for syntax highlighting in code blocks.
To use the same color scheme in both modes,
set only :confval:`sphinx:pygments_style`:

.. code-block:: python
   :caption: |conf|

   pygments_style = "xcode"

To use different color schemes for light mode and dark mode,
set ``pygments_style`` and ``pygments_style_dark``.
For example, this documentation uses ``xcode`` in light mode and ``github-dark`` in dark mode:

.. code-block:: python
   :caption: |conf|

   pygments_style = "xcode"
   pygments_style_dark = "github-dark"

Both schemes use muted colors. These colors suit the neutral palette of the theme.
You can also try these Pygments color schemes:

- Light mode: ``default``, ``friendly``, ``vs``
- Dark mode: ``one-dark``, ``nord``, ``night-owl``

Do not use highly saturated color schemes, such as ``monokai`` or ``dracula``. They can clash with the rest of the theme.

After you select the color schemes, check code blocks in light mode and dark mode.
Make sure that text, highlighted tokens, and line numbers have enough contrast.
A color scheme designed for one mode might not work in the other mode.

To change the background of code blocks, :ref:`add custom CSS <sec:custom-css>`.
For example, this CSS makes the background transparent in both modes:

.. code-block:: css

   :root:not(.dark) .highlight,
   :root.dark .highlight {
      background-color: transparent;
   }

You can replace ``transparent`` with another CSS color.
Check the contrast again after you change the background.

.. note::

   If you set ``pygments_style``, code blocks keep the background and text colors of that scheme.
   If you set ``pygments_style_dark``, the theme uses it in dark mode, with its background and text colors.
   If you set neither, the theme sets the background of code blocks to match the page.
   The dark scheme follows the theme toggle, not the operating system setting.
