How to modify the theme
=======================

Depending on how much you want to modify the theme,
use one of these options.

.. contents:: On this page
   :local:
   :backlinks: none

Adding or overriding styles
---------------------------

To override or add additional JavaScript and CSS,
you don't need to install the theme's dependencies.

To add additional CSS files,
use the `html_css_files`_ configuration value.
To add additional JavaScript files, use the `html_js_files`_
configuration value.

.. _html_css_files: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_js_files
.. _html_js_files: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_css_files

For example, place additional styles in a file :file:`_static/custom.css`
and add the following options to your Sphinx configuration in :file:`conf.py`:

.. code-block:: python
   :caption: conf.py

   html_static_path = ["_static"]
   html_css_files = ["custom.css"]

If you want to override existing styles,
you might have to add ``!important``.
For more information, see the
`Mozilla Developer Networks <https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity>`_.

.. note::

   Since these additional CSS and JavaScript files aren't
   parsed by Webpack, use your own styles and don't use
   Tailwind's ``@apply`` directive.


Modifying the templates
-----------------------

Styles in the templates are applied via Tailwind's utility classes.

.. code-block:: console
   :emphasize-lines: 1

   ./src/
   ├sphinxawesome_theme/
   └theme-src/

To modify these styles, follow these steps:

#. Install the Python and JavaScript dependencies.

   See :ref:`Setting up a development environment` for more information.

#. Make your change.

   For example, to change the background color of the header to orange,
   open :file:`sphinxawesome_theme/header.html` and change:

   .. code-block:: html
      :emphasize-removed: 1
      :emphasize-added: 2

      <header class="md:sticky top-0 bg-gray-900 ...">
      <header class="md:sticky top-0 bg-orange-500 ...">

#. Build the theme.

   .. code-block:: console

      $ yarn build

Modifying CSS files
-------------------

Everything that's part of the main content,
including everything that's converted from reStructuredText to HTML
is styled using Tailwind's ``@apply`` directive.

.. code-block:: console
   :emphasize-lines: 3

   ./src/
   ├sphinxawesome_theme/
   └theme-src/
    └css/

To modify these styles, follow these steps:

#. Install the Python and JavaScript dependencies.

   See :ref:`Setting up a development environment` for more information.

#. Make your change.

   The CSS files are arranged according to the elements they apply to.
   For example, if you want to change the appearance of links from the default blue to an
   orange, open :file:`theme-src/css/links.css` and change:

   .. code-block:: css
     :force:
     :emphasize-removed: 7
     :emphasize-added: 8

     p:not(.admonition-title),
     .nav-toc,
     .search,
     .toctree-wrapper,
     .contents.local {
       & a {
         @apply text-blue-700;
         @apply text-orange-500;
       }
     }

#. Build the theme.

   .. code-block:: console

      $ yarn build
