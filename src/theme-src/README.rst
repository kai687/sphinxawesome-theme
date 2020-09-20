JavaScript and CSS sources
--------------------------

This directory contains all necessary files to build the static assets of the theme,
used to style the HTML and add functionality to improve the user experience.

::

   theme-src/
   ├── css/
   ├── js/
   ├── app.js
   ├── package.json
   ├── postcss.config.js
   ├── tailwind.config.js
   └── webpack.config.js

To build the static assets, you need `Node.js`_.
Use your preferred version to install Node.js if you have any—I like nvm_.
I also prefer yarn_ over npm. To install ``yarn`` globally, enter::

   $ npm install -g yarn

Next, install the project's dependencies::

   $ yarn install

To build the static assets, enter::

   $ yarn build

This executes ``webpack`` in production mode.
The entry point is the file ``app.js``.
This file imports all CSS files, and imports
and calls the JavaScript functions.
The CSS is extracted and put in a file ``theme.css``.
The JavaScript is bundled and put into a file ``theme.js``.
Both files are placed in the ``static/`` folder.
of the ``sphinxawesome_theme/`` directory.

The CSS is processed with PostCSS_ using a couple of plugins.
The most important plugin is TailwindCSS_.
The theme uses Tailwind to style the website.
The theme also uses the postcss-import_ plugin, to be able to
import other CSS modules, and the postcss-preset-env_ plugin,
which enables modern CSS features like nesting, custom selectors, etc.
At the end, cssnano_ minifies the resulting CSS.

The CSS is checked with stylelint_.
The rules are defined in the file ``package.json``.

The JavaScript files are loaded with babel_ and checked with eslint_
before being bundled and minified.

.. _ Node.js: https://nodejs.org/en/
.. _ nvm: https://github.com/nvm-sh/nvm
.. _ yarn: https://classic.yarnpkg.com/lang/en/
.. _ PostCSS: https://postcss.org/
.. _ TailwindCSS: https://tailwindcss.com/
.. _ postcss-import: https://github.com/postcss/postcss-import
.. _ postcss-preset-env: https://github.com/csstools/postcss-preset-env
.. _ cssnano: https://cssnano.co/
.. _ stylelint: https://stylelint.io/
.. _ babel: https://babeljs.io/
.. _ eslint: https://eslint.org/
