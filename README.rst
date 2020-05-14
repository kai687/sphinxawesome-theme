====================
Sphinx Awesome Theme
====================

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
   :alt: MIT license

This is a simple but awesome theme for the `Sphinx
<http://www.sphinx-doc.org/en/master/>`_ documentation generator.


------------
Installation
------------

Install the theme as a Python package:

.. code:: console

   $ pip install sphinxawesome-theme

To use the theme, set the ``html_theme`` variable in the Sphinx configuration file
``conf.py``:

.. code:: python

   html_theme = "sphinxawesome_theme"

.. include-until-here

-------------
Configuration
-------------

To show entries in the navigation menu that come from `toctree
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html?highlight=toctree#directive-toctree>`_
directives with the ``:hidden:`` option, add the following setting to the Sphinx
configuration file ``conf.py``.

.. code:: python

   html_theme_options = {"nav_include_hidden": True}

The default is ``False`` to be in line with other themes. Including ``:hidden:`` to a
toctree directive makes Sphinx include the documents, but not print the list of links to
the documents. Combining the ``:hidden:`` option with the ``nav_include_hidden`` option
allows the links to the included documents to be shown in the navigation menu, but avoid
the duplicated links on the content pages.


-------------
Documentation
-------------

Read the documentation and see how the theme looks over there.
