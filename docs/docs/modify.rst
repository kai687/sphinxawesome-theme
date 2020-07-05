=======================
How to modify the theme
=======================

.. note::

   If you want to modify the theme,
   you need `Node.js <https://nodejs.org/en/>`_.
   If you just want to use the theme
   or override some of the styles,
   you don't need Node.js.

Follow these steps to modify the theme:

#. :ref:`Clone the repository <How to install the theme>`.
#. Change to the directory :dir:`./sphinxawesome-theme`.
   It has the following structure:

   .. vale off

   .. code-block:: console
      :emphasize-lines: 4

      ./sphinxawesome-theme/
        ├src/
        │ ├sphinxawesome_theme/
        │ └theme-src/
        ├docs/
        └...

   .. vale on

#. Change to the :dir:`theme-src` directory
   and install the JavaScript dependencies:

   .. code-block:: console

      $ npm install


---------------------------
Adding or overriding styles
---------------------------

You can add additional CSS files via
`html_css_files
<https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_css_files>`_
and additional JavaScript files via
`html_js_files
<https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_js_files>`_.

For example, place additional styles in a file :file:`_static/custom.css`
and add the following options
to your Sphinx configuration in :file:`conf.py`::

   html_static_path = ["_static"]
   html_css_files = ["custom.css"]

If you want to override existing styles,
you might have to add ``!important``.

.. note::

   If the styles are applied via classes,
   they have a higher specificity
   than targeting the element itself.
   For example, a ``<h1 class="text-red-600">`` will appear red
   even if your custom CSS overrides the text color for all ``h1`` elements.
   Adding ``!important`` to the custom CSS style ensures
   that the style gets the highest specificity.
   Use ``!important`` only when necessary.
   For more information, see the
   `Mozilla Developer Networks web docs <https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity>`_.


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
This includes everything that's converted from reStructuredText to HTML
and part of the navigation menu.

These styles are defined in :file:`theme-src/src/theme-custom.css`.

Everything that's not converted from reStructuredText is styled
with Tailwind's classes directly. This includes most elements on the page
surrounding the "main" element, for example
for example the header, the footer, or the background.

These styles are defined in the template files in :dir:`sphinxawesome_theme`.

After making changes, either in the template files or in :file:`theme-custom.css`,
rebuild the theme:

.. code-block:: console

   $ npm run build

.. rubric:: Examples

For example, if you want to change the appearance of links from the default blue to an
orange, open :file:`theme-custom.css` and change:

.. code-block::

   p a {
     @apply text-blue-600;
   }

to:

.. code-block::

   p a {
     @apply text-orange-600;
   }

For example, to change the background color of the header to orange,
open :file:`sphinxawesome_theme/header.html` and change:

.. code-block:: html

   <header class="md:sticky top-0 bg-white ...">

to:

.. code-block:: html

   <header class="md:sticky top-0 bg-orange-500 ...">
