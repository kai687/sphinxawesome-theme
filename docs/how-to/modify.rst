=======================
How to modify the theme
=======================

First, follow the steps in :ref:`Setting up a development environment`
to install the Python and JavaScript dependencies.

---------------------------
Adding or overriding styles
---------------------------

You can add additional CSS files via the `html_css_files`_
configuration value,
and additional JavaScript files via `html_js_files`_

.. _html_css_files: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_js_files
.. _html_js_files: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_css_files

For example, place additional styles in a file :file:`_static/custom.css`
and add the following options to your Sphinx configuration in :file:`conf.py`::

   html_static_path = ["_static"]
   html_css_files = ["custom.css"]

If you want to override existing styles,
you might have to add ``!important``.
For more information, see the
`Mozilla Developer Networks <https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity>`_.

.. note::

   Additional CSS and JavaScript files are not included
   in the ``webpack`` configuration,
   that means you can't use Tailwind's classes in these
   additional files.

---------------------
Which files to modify
---------------------

The sources of the theme are structured as follows:

.. code-block:: console

   src/
   ├sphinxawesome_theme/
   └theme-src/

This theme uses CSS styles in two ways.
Everything that's part of the main content
is styled via Tailwind's ``@apply`` directives.
This includes everything that's converted from reStructuredText to HTML.

These styles are defined in the files :file:`theme-src/css/*.css`.
The CSS is categorized according to the elements which they apply to.
For instance, styles relevant for the navigation menu are in :file:`nav.css`.

Everything that's not converted from reStructuredText is styled
with Tailwind's classes directly in the template files.
This includes most elements on the page
except the "main" element, for example
for example the header, the footer, or the background.

These styles are defined in the template files in :dir:`sphinxawesome_theme`.

After making changes, either in the template files or in the CSS files,
rebuild the theme:

.. code-block:: console

   $ yarn build

.. rubric:: Examples

For example, if you want to change the appearance of links from the default blue to an
orange, open :file:`links.css` and change:

.. code-block:: css
   :force:
   :emphasize-removed: 3
   :emphasize-added: 4

   p:not(.admonition-title) a,
   #nav-toc a {
      @apply text-blue-700;
      @apply text-orange-600;
   }

For example, to change the background color of the header to orange,
open :file:`sphinxawesome_theme/header.html` and change:

.. code-block:: html
   :emphasize-removed: 1
   :emphasize-added: 2

   <header class="md:sticky top-0 bg-white ...">
   <header class="md:sticky top-0 bg-orange-500 ...">
