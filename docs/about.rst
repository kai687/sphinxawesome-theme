=====
About
=====

This page contains information about used external assets
as well as topics that didn't really fit anywhere else.


------
Assets
------

The sphinx awesome theme relies on the following external assets.
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
The Roboto fonts are bundled in the theme's static directory.
The CSS for the tooltips was copied into the file :file:`tooltips.css` and adapted
to use Tailwind's classes where feasible.

.. vale on


-----------------
How does it work?
-----------------

Sphinx :term:`themes <theme>` are a collection of HTML templates,
CSS styles and JavaScript files. Sphinx uses the Jinja2 templating
language. The main template is in the file :file:`layout.html`, which
imports all other components, such as header, navigation bar, the
main content area, and so on.

The Sphinx awesome theme uses the Tailwind CSS framework,
which is a nice way to compose websites from scratch without
having to worry about selectors, specificity and interference--
utility first, abstractions later.

Although the HTML produced by Sphinx and the underlying docutils module
often looks old-fashioned, Sphinx is a very flexible tool,
where almost everything can be modified. This theme changes a lot of
those aspects during build time. The biggest feature here is
the *awesome code block*. See the demo pages for a feature overview.

.. TODO ^ insert xref to demo page or README.

Not everything is as easy as it could be, or at least,
not as easy to understand as it could be. Sometimes,
some minor modifications require almost a full re-implementation
of a method, which I have done at times, only to deviate
a tiny bit from the default on one or two lines.

Maybe in the future, the API will be improved such that it is easier
to modify parts of the transformation without having to copy and
paste whole chunks of code from the docutils or Sphinx repository.
For the present, I found it easier to just parse the HTML again
with BeautifulSoup.

------------------------------
Package and project management
------------------------------

The project is distributed as a Python package. Three tools are vital in order to achieve this:

- `Poetry <https://python-poetry.org/>`_
- `Nox <https://nox.thea.codes/en/stable/>`_
- `pre-commit <https://https://pre-commit.com/>`_

Building the packages and Poetry is a Python package manager, that uses a :file:`pyproject.toml` file to declare
all the project's dependencies, and is used to build the package and upload it to PyPI.

Nox is an automation tool that is used to perform various tests and checks, as well as
building the documentation.

Pre-commit is a tool, that runs configurable checks on every ``git commit``.

The JavaScript and CSS portions of the theme are managed by Webpack_.  The entry point
for Webpack is the file `app.js`_.  In this file, all dependencies are imported
(including fonts and CSS styles) and the custom JavaScript functions are defined.  The
Webpack configuration `webpack.config.js`_ instructs Webpack how to process the CSS,
JavaScript, and fonts.  The JavaScript is checked with ESLint_ minified and put in the
output directory.  This file is read and run by the browser.  The fonts are imported
from ``npm`` packages and also copied to the output directory.

The CSS is checked with stylelint_ and passed through PostCSS_ with a few plugins,
defined in the configuration file `postcss.config.js`_.  The most important PostCSS
plugins are Tailwind_ and PurgeCSS_.  Tailwind defines a lot of classes for consistent
styling and easy composition, at the cost of a large output CSS file if left
unprocessed. PurgeCSS goes through all CSS files and HTML templates and removes from the
final CSS all Tailwind classes that aren't used.  For example, if the theme never uses
any ``text-purple-*`` classes, they will not appear in the final output, thus greatly
reducing the final size of the CSS file.

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
.. _webpack.config.js: https://github.com/kai687/sphinxawesome-theme/blob/master/src/theme-src/webpack.config.js
.. _app.js: https://github.com/kai687/sphinxawesome-theme/blob/master/src/theme-src/app.js
.. _ESLint: https://eslint.org/
.. _stylelint: https://stylelint.io/
.. _PostCSS: https://postcss.org
.. _postcss.config.js: https://github.com/kai687/sphinxawesome-theme/blob/master/src/theme-src/postcss.config.js
.. _Tailwind: https://tailwindcss.com
.. _PurgeCSS: https://purgecss.com
.. _Docutils: https://docutils.sourceforge.io/
.. _BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/
