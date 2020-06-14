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

The icons have been copied and included as SVG directly in the HTML templates.
The Roboto fonts are bundled in the theme's static directory.


-----------------
How does it work?
-----------------

Sphinx themes are a collection of Jinja2_ templates for the HTML, CSS styles and
additional JavaScript files.
The traditional way to style a theme is to write conventional CSS.
After that, all that needs to be done to use the theme
is to put files in the right place for Sphinx.

I wanted to try something different.
Instead of writing CSS completely separate from the HTML where it's needed,
I was intrigued by the idea behind Tailwind_.
With the help of Tailwind CSS it wasn't that difficult to come up
with a new design from scratch relatively fast.

Tailwind has a lot of classes.
If you include all of them,
the final CSS file will be quite large.
Luckily, the classes do not interfere with each other,
so that unused styles can be removed from the final CSS quite easily using PurgeCSS_.

Since I also added a few JavaScript functions
to open and close menus,
add the 'copy code block' button and other small things,
I wanted to use a tool
that can handle all the aspects of CSS and JavaScript manipulation for me.
Enter Webpack_.

The theme is built using ``webpack`` which is executed as an ``npm`` (or yarn) script.
The entry point is :file:`theme-src/src/theme-src.js`.
This file includes all JavaScript functions
and it imports all dependencies,
such as the fonts and the CSS.

The Webpack configuration :file:`theme-src/webpack.config.js` instructs webpack
what to do with the CSS, JavaScript, and fonts.
The JavaScript is *minified* and put in the output directory
:dir:`sphinxawesome_theme/static`.
This file is read and executed by the browser.
The fonts are imported from ``npm`` packages and also copied to the output directory.
The ``npm`` packages also create the ``@fontface`` rules for the CSS.
The CSS is processed with PostCSS_.
The configuration in :file:`theme-src/postcss.config.js` uses a few plugins,
including Tailwind and PurgeCSS.

PurgeCSS will go through all template HTML files
and remove from the final CSS all Tailwind classes that are not used.
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
