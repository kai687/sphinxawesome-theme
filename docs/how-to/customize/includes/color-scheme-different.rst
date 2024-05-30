Select different color schemes for light and dark modes
-------------------------------------------------------

If you want to use different color schemes for syntax highlighting in light and dark mode,
follow these steps:

#. Select a theme you want to use in light mode and :ref:`set it as your color scheme <sec:set-color-scheme>` with the ``pygments_style`` option.
#. Select a color scheme you want to use in dark mode and run the following command:

   .. code-block:: sh
      :emphasize-text: THEME

      pygmentize -s THEME -f html -a .dark > pygments-dark.css

   This runs the ``pygmentize`` command, which is part of the Pygments package.
   If you installed the |product|, Pygments is also installed.

#. Add the file :file:`pygments-dark.css` as :ref:`custom css <sec:custom-css>`.

.. dropdown:: More information

   Themes can define ``pygments_style`` and ``pygments_style_dark`` options in their :file:`themes.conf` file.
   This applies different color schemes in light and dark mode based on the system settings and the ``prefers-color-scheme`` media query.
   However, this doesn't work with manual theme switchers that select different CSS based on classes.
   Therefore, we have to add the styles for dark mode as custom CSS.
