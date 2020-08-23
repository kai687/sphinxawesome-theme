=====
About
=====

This page contains information about used external assets
as well as topics that didn't really fit anywhere else.


------
Assets
------

The sphinx awesome theme relies on the following external assets.

.. list-table::
   :header-rows: 1

   * - Purpose
     - Name/Website
   * - CSS framework
     - `Tailwind <https://tailwindcss.com>`_
   * - fonts
     - `Roboto <https://github.com/googlefonts/roboto>`_
   * - icons for menu and magnifying glass
     - `Entypo <http://www.entypo.com>`_ by Daniel Bruce
   * - icons for copy buttons in code blocks
     - `Zondicons <http://www.zondicons.com>`_ by Steve Schoger

.. vale off

The icons are copied and included as SVG directly in the HTML templates.
The Roboto fonts are bundled in the theme's static directory.

.. vale on


-----------------
How does it work?
-----------------

Sphinx themes are a collection of Jinja2_ templates for the HTML, CSS styles and
additional JavaScript files.
The traditional way to style a theme is to write conventional CSS.
After that, you just need to put the files in a place that Sphinx can find
in order to use the theme.

.. vale off

I wanted to try something different.
Instead of writing CSS separate from the HTML where it's needed,
I was intrigued by the idea behind Tailwind_.
With the help of Tailwind CSS it wasn't that difficult to come up
with a new design from scratch relatively fast.

Tailwind has a lot of classes.
If you include all of them,
the final CSS file is quite large.
Luckily, the classes don't interfere with each other,
so that unused styles can be removed from the final CSS quite easily using PurgeCSS_.

Since I also added a few JavaScript functions,
I wanted to include a tool
that can handle all the aspects of CSS and JavaScript manipulation for me.
Enter Webpack_.

.. vale on

The theme is built using ``webpack`` which is executed as an ``npm`` (or yarn) script.
The entry point is :file:`theme-src/src/theme-src.js`.
This file includes all JavaScript functions
and imports all dependencies,
such as the fonts and the CSS.

The Webpack configuration :file:`theme-src/webpack.config.js` instructs webpack
how to process the CSS, JavaScript, and fonts.
The JavaScript is *minified* and put in the output directory
:dir:`sphinxawesome_theme/static`.
This file is read and executed by the browser.
The fonts are imported from ``npm`` packages and also copied to the output directory.
The ``npm`` packages also create the ``@fontface`` rules for the CSS.
The CSS is processed with PostCSS_.
The configuration in :file:`theme-src/postcss.config.js` uses a few plugins,
including Tailwind and PurgeCSS.

PurgeCSS goes through all template HTML files
and removes from the final CSS all Tailwind classes that aren't used.
For example, if the theme never uses any ``text-purple-*`` classes,
they will not appear in the final output,
thus greatly reducing the final size of the CSS file.
Finally, the CSS will also be *minified*.

.. note::

   Minification is the process of removing all unnecessary whitespace from the final
   output. In JavaScript, variable names are often abbreviated with a single letter.
   This can greatly reduce the file size, thus improving performance.

.. _Jinja2: https://jinja.palletsprojects.com
.. _Tailwind: https://tailwindcss.com
.. _Webpack: https://webpack.js.org
.. _PurgeCSS: https://purgecss.com
.. _PostCSS: https://postcss.org


------------------------------
Package and project management
------------------------------

The project is distributed as a Python package. Three tools are vital in order to achieve this:

- `Poetry <https://python-poetry.org/>`_
- `Nox <https://nox.thea.codes/en/stable/>`_
- `pre-commit <https://https://pre-commit.com/>`_

Poetry is a Python package manager, that uses a :file:`pyproject.toml` file to declare
all the project's dependencies, and is used to build the package and upload it to PyPI.

Nox is an automation tool that is used to perform various tests and checks, as well as
building the documentation.

Pre-commit is a tool, that runs configurable checks on every ``git commit``.
