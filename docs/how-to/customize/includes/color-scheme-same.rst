.. _sec:set-color-scheme:

Select color schemes for syntax highlighting
--------------------------------------------

Syntax highlighting is provided by the Pygments library and the *bw* color scheme.
To select a different color scheme **for both light and dark mode**,
use the :confval:`sphinx:pygments_style` option:

.. code-block:: python
   :caption: |conf|
   :emphasize-text: PYGMENTS_THEME

   pygments_style = "PYGMENTS_THEME"

For a list of available themes, see the Pygments_ documentation.
For even more themes, see the `accessible pygments themes`_ project.

.. _Pygments: https://pygments.org/styles/
.. _accessible pygments themes: https://github.com/Quansight-Labs/accessible-pygments
