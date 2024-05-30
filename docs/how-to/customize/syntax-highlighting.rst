.. meta::
   :description: Select syntax highlighting color schemes.
   :twitter:description: Select syntax highlighting color schemes.

Select color schemes for syntax highlighting
============================================

.. rst-class:: lead

   Select different color schemes for syntax highlighting in code blocks.

With Sphinx, syntax highlighting is provided by the Pygments_ library.
The |product| uses the built-in **bw** theme with a transparent background.
This works equally well in light and dark mode.

To select a different color scheme **for both light and dark mode**,
use the :confval:`sphinx:pygments_style` option:

.. code-block:: python
   :caption: Do something
   :emphasize-text: PYGMENTS_THEME

   pygments_style = "PYGMENTS_THEME"


.. _Pygments: https://pygments.org/styles/
