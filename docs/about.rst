About
=====

This page is a collection of topics about the sphinx awesome theme.

Assets
------

The sphinx awesome theme uses the following external assets.

.. list-table::
   :header-rows: 1

   * - For
     - Name/Website
   * - CSS
     - `Tailwind <https://tailwindcss.com/>`_
   * - fonts
     - `Roboto <https://github.com/googlefonts/roboto>`_
   * - icons for menu and magnifying glass
     - `Entypo <http://www.entypo.com/>`_ by Daniel Bruce
   * - icons for copy buttons in code blocks
     - `Zondicons <http://www.zondicons.com/>`_ by Steve Schoger


Technology
----------

Building the theme involves a few technologies. At the top layer is `Webpack
<https://webpack.js.org/>`_ that ties everything together. The entry point is in
``theme-src/src/theme-src.js`` which includes both all JavaScript functions that provide
some simple interactions in the theme, and all dependencies, such as the fonts and the
styles.

The JavaScript is bundled and minified into the ``sphinxawesome_theme/static/theme.js``,
which will be read by the browser.

The fonts are read from the npm packages ``typeface-roboto`` and
``typeface-roboto-mono``, which both have the web fonts and also create the
``@fontface`` rules for the CSS.

The styles are read from ``theme-src/src/theme-src.css``, which are the basic `tailwind
directives <https://tailwindcss.com/docs/installation#2-add-tailwind-to-your-css>`_. The
file ``theme-src/src/theme-custom.css`` contains all styles for elements that come
directly from Sphinx, such as headings, tables, paragraph text, etc. These files are
processed by `PostCSS <https://postcss.org/>`_ and in particular the `PurgeCSS
<https://purgecss.com/>`_ plugin. This checks the HTML templates and removes unused
classes from the final ``sphinxawesome_theme/static/theme.css`` file.


Overriding the theme
--------------------

This themes supports the standard mechanism of adding additional CSS via `html_css_files
<https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_css_files>`_
and additional JavaScript files via `html_js_files
<https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_js_files>`_.

For example, place additional styles in a file ``_static/custom.css`` and add the
following options to your Sphinx configuration in ``conf.py``:

.. code-block:: python

   html_static_path = ["_static"]
   html_css_files = ["custom.css"]

You might have to add ``!important`` to override the styles of some elements, if the
base theme's styles have a higher specificity, for example, when applied via Tailwind's
classes.
