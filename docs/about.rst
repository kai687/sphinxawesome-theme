:orphan: true
:layout: without-sidebar

.. meta::
   :description: The Awesome Sphinx Theme is built on top of open source assets.

About
=====

.. rst-class:: lead

   This pages lists assets that the |product| uses to be awesome.

----

To see the full list of dependencies, see these files:

- :gh:`pyproject.toml` for Python dependencies
- :gh:`package.json <src/theme-src/package.json>` for JavaScript dependencies

+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
| Feature                                                 | Name/Website                  | License                                                                           |
+=========================================================+===============================+===================================================================================+
| CSS framework                                           | Tailwind_                     | `MIT License <https://github.com/tailwindlabs/tailwindcss/blob/master/LICENSE>`__ |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
| Copy to clipboard                                       | Clipboard.js_                 | `MIT License <https://github.com/zenorocha/clipboard.js/blob/master/LICENSE>`__   |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
| Fonts                                                   | Roboto_                       | `Apache License, Version 2.0`_                                                    |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
|                                                         | `JetBrains Mono`_             | `SIL Open Font License, 1.1`_                                                     |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
| Icons                                                   | `Material icons`_             | `Apache License, Version 2.0`_                                                    |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
| Tooltips                                                | `Primer/CSS`_                 | `MIT License <https://github.com/primer/css/blob/main/LICENSE>`__                 |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
| **Note:** versions ≤ 1.13.1 used these icons instead:   | Entypo_ by Daniel Bruce       | `Creative Commons Attribution-ShareAlike 4.0`_                                    |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
|                                                         | Zondicons_ by Steve Schoger   | ?                                                                                 |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
| Illustrations                                           | undraw.co_                    | custom_                                                                           |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+

.. _Tailwind: https://tailwindcss.com
.. _Clipboard.js: https://clipboardjs.com
.. _Roboto: https://github.com/googlefonts/roboto
.. _JetBrains Mono: https://github.com/JetBrains/JetBrainsMono/
.. _SIL Open Font License, 1.1: https://github.com/JetBrains/JetBrainsMono/blob/master/OFL.txt
.. _Material icons: https://fonts.google.com
.. _undraw.co: https://undraw.co
.. _custom: https://undraw.co/license
.. _Primer/CSS: https://primer.style/css/
.. _Entypo: http://www.entypo.com
.. _Zondicons: http://www.zondicons.com
.. _Creative Commons Attribution-ShareAlike 4.0: https://creativecommons.org/licenses/by-sa/4.0/legalcode
.. _Apache License, Version 2.0: https://www.apache.org/licenses/LICENSE-2.0.html

Breaking changes
----------------

Updating the |product| is straightforward in most cases.
If you use any customization, you might have to update your
customizations manually.

Version 4.0
~~~~~~~~~~~

Version 4.0 of the |product| includes these **breaking changes**:

Add support for Sphinx 6
   Since Sphinx 6 is only supported with the latest version of the `myst-parser` package
   and Sphinx 6 drops support for Python 3.7, this release is a major version update.

Apart from that, this version is identical with version 3 of the |product|.

Version 3.0
~~~~~~~~~~~

Redesign
   Create a better visual hierarchy which makes the document easier to scan.
   Heavily inspired by the `Material Design <https://m2.material.io/>`_ website.

Restructure
   All JavaScript is now using the `Stimulus <https://stimulus.hotwired.dev/>`_ framework.

Version 2.0
~~~~~~~~~~~

Version 2.0 of the |product| includes these **breaking changes**:

Require Sphinx 4 or newer
   Sphinx 4 depends on docutils 0.17, which creates more semantic HTML by default.
   This allows to reduce the amount of custom transformations.

Restructure several templates
   The layout use `CSS grid <https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout>`_.
   This leads to fewer container elements in the templates.
