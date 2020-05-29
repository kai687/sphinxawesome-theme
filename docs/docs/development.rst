=======================
How to modify the theme
=======================

.. note::

   If you want to modify the theme, you need `Node.js <https://nodejs.org/en/>`_. If
   you just want to use the theme or override some of the styles, you don't need
   Node.js.

First, :ref:`clone the repository <How to install the theme>`. Next, change to the directory
``./sphinxawesome-theme/theme-src/`` and install the dependencies for building the theme.

.. code-block:: console

   npm install


---------------------------
Adding or overriding styles
---------------------------

You can add additional CSS files via `html_css_files
<https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_css_files>`_
and additional JavaScript files via `html_js_files
<https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_js_files>`_.

For example, place additional styles in a file ``_static/custom.css`` and add the
following options to your Sphinx configuration in ``conf.py``:

.. code-block:: python

   html_static_path = ["_static"]
   html_css_files = ["custom.css"]

If you want to override existing styles, you might have to add ``!important``.

.. note::

   If the styles are applied via classes, they have a higher specificity than targeting
   the element itself. For example, a ``<h1 class="text-red-600">`` will appear red
   even if your custom CSS overrides the text color for all ``h1`` elements. Adding
   ``!important`` to the custom CSS style will ensure that the style gets the highest
   specificity. Use ``!important`` only when necessary. For more information, check the
   `MDN web docs <https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity>`_.


---------------------
Which files to modify
---------------------

This theme uses CSS styles in two ways. Everything, that is part of the main content,
that is, everything that is converted from reStructuredText to HTML is styled via
Tailwind's ``@apply`` directive. This also includes the navigation list in the menu on
the left side.

These styles are in the ``theme-src/`` directory. This directory contains everything
that is necessary to “build” the final CSS and JavaScript for Sphinx. The custom styles
themselves are in the file ``theme-src/src/theme-custom.css``.

Everything that is not part of the conversion, but are part of the structure of the
page, for example the header, the footer, or the background, is styled by applying
Tailwind's classes directly in the template files, which are in the
``sphinxawesome_theme/`` directory.

After modifying the changes, rebuild the CSS:

.. code-block:: console

   npm run build

.. rubric:: Examples

For example, if you want to change the appearance of links from the default blue to an
orange, open the file ``theme-src/src/theme-custom.css`` and change:

.. code-block::

   p a {
     @apply text-blue-600;
   }

to:

.. code-block::

   p a {
     @apply text-orange-600;
   }

For example, to change the background color of the header to orange, open the file
``sphinxawesome_theme/header.html`` and change:

.. code-block:: html

   <header class="md:sticky top-0 bg-white ...">

to:

.. code-block:: html

   <header class="md:sticky top-0 bg-orange-500 ...">


----------------------------------
Using a local version of the theme
----------------------------------

If you want to use a modified version of the theme for your documentation, you can use
the theme locally. To keep your project tidy, you can place it inside a directory
``_ext``, or ``_themes`` in the top-level directory.

For example, if you have a project structure like this:

.. code-block:: console

   ./
   ├conf.py
   ├index.rst
   └_ext

Change to the ``_ext`` directory and :ref:`clone the repository <How to install the theme>`.
Next, modify your Sphinx configuration file ``conf.py``:

.. code-block:: python

   html_theme = "sphinxawesome_theme"
   html_theme_path = ["_ext/sphinxawesome-theme"]

If you build the documentation now, it uses the local version of the theme.
