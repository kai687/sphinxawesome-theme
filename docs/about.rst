About
=====

This page contains information about used external assets
as well as topics that didn't really fit anywhere else.

Assets
------

The Sphinx awesome theme relies on the following external assets.
For a full list of dependencies, see the file :file:`pyproject.toml`
for Python dependencies and :file:`package.json` for JavaScript dependencies.

.. list-table::
   :header-rows: 1

   * - Purpose
     - Name/Website
     - License
   * - CSS framework
     - `Tailwind <https://tailwindcss.com>`_
     - `MIT License <https://github.com/tailwindlabs/tailwindcss/blob/master/LICENSE>`__
   * - Select and copy stuff
     - `Clipboard.js <https://clipboardjs.com/>`_
     - `MIT License <https://github.com/zenorocha/clipboard.js/blob/master/LICENSE>`__
   * - Fonts
     - `Roboto <https://github.com/googlefonts/roboto>`_
     - `Apache License, Version 2.0`_
   * - Icons
     - `Material icons <https://material.io/resources/icons/>`_
     - `Apache License, Version 2.0`_
   * - Tooltips
     - `Primer/CSS <https://primer.style/css/>`_
     - `MIT License <https://github.com/primer/css/blob/master/LICENSE>`__
   * - **Note:** versions ≤ 1.13.1 used these icons instead:
     - `Entypo <http://www.entypo.com>`_ by Daniel Bruce
     - `Creative Commons Attribution-ShareAlike 4.0`_
   * -
     - `Zondicons <http://www.zondicons.com>`_ by Steve Schoger
     - ?

.. _Creative Commons Attribution-ShareAlike 4.0: https://creativecommons.org/licenses/by-sa/4.0/legalcode
.. _Apache License, Version 2.0:  https://www.apache.org/licenses/LICENSE-2.0.html

.. vale off

The icons are copied and included as SVG directly in the HTML templates.
The fonts are bundled in the theme's static directory.
The CSS for the tooltips was copied into the file :file:`tooltips.css` and adapted
to use Tailwind's classes where feasible.

.. vale on

How does it work?
-----------------

Sphinx themes are a collection of HTML templates, CSS styles and JavaScript files.
Sphinx uses the Jinja2 templating language.
The main template is in the file :file:`layout.html`,
which defines the overall structure of the page,
loads the CSS and JavaScript files,
and imports other components, such as the header or navigation menu.
The main content is rendered into a template file :file:`page.html`,
which extends the main layout and renders the ``body`` text.

The Sphinx awesome theme defines a number of internal extensions.
The transformation of the reStructuredText sources to HTML is modified
to produce less nested and more modern HTML, for example,
using semantic HTML elements where feasible.

Some parts of the Sphinx/docutils toolchain are difficult to extend,
and modifying a single line would result in copying and pasting
the whole method. In such cases, the changes are implemented in a
postprocessing extension that uses BeautifulSoup_ to parse the built HTML
again.

Package and project management
------------------------------

The project is distributed as a Python package.
The following tools are vital in order to achieve this:

- `Poetry <https://python-poetry.org/>`_
- `Nox <https://nox.thea.codes/en/stable/>`_
- `pre-commit <https://https://pre-commit.com/>`_

The JavaScript and CSS portions of the theme are managed by Webpack_.
The entry point for Webpack is the file `app.js`_.
In this file, all dependencies are imported
(including fonts and CSS styles).

The JavaScript is checked with ESLint_, minified, and put in the output directory.
This file is read and run by the browser.

The CSS is checked with stylelint_ and passed through PostCSS_ with a few plugins.
Tailwind is defined as a plugin and processes the templates *and* CSS files,
where it parses the ``@apply`` directives.
Since Tailwind defines a lot of classes that won't be used in the final project,
PurgeCSS_ is used by Tailwind to remove these unused classes from the final CSS file.

.. seealso::

   - Webpack_
   - ESLint_
   - Stylelint_
   - PostCSS_
   - PurgeCSS_
   - Jinja2_
   - Docutils_
   - BeautifulSoup_


.. _Jinja2: https://jinja.palletsprojects.com
.. _Webpack: https://webpack.js.org
.. _app.js: https://github.com/kai687/sphinxawesome-theme/blob/master/src/theme-src/app.js
.. _ESLint: https://eslint.org/
.. _stylelint: https://stylelint.io/
.. _PostCSS: https://postcss.org
.. _Tailwind: https://tailwindcss.com
.. _PurgeCSS: https://purgecss.com
.. _Docutils: https://docutils.sourceforge.io/
.. _BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/
