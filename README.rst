====================
Sphinx Awesome Theme
====================

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
   :alt: MIT license
   :class: badge

.. image:: https://api.netlify.com/api/v1/badges/e6d20a5c-b49e-4ebc-80f6-59fde8f24e22/deploy-status
   :target: https://app.netlify.com/sites/confident-austin-7d4cfd/deploys
   :alt: Netlify Status
   :class: badge

This is a simple but awesome theme for the `Sphinx
<http://www.sphinx-doc.org/en/master/>`_ documentation generator.


------------
Installation
------------

Install the theme as a Python package:

.. code:: console

   pip install sphinxawesome-theme

To use the theme, set ``html_theme`` in the Sphinx configuration file
``conf.py``:

.. code:: python

   html_theme = "sphinxawesome_theme"

-------------
Configuration
-------------

To show also entries in the navigation menu from `toctree
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html?highlight=toctree#directive-toctree>`_
directives with the ``:hidden:`` option, add the following setting to the Sphinx
configuration file ``conf.py``.

.. code:: python

   html_theme_options = {"nav_include_hidden": True}

Including ``:hidden:`` in a toctree directive makes Sphinx include the documents, but
not print the list of links to the documents. This can be useful if a theme (such as
this theme) has a separate navigation menu. ``nav_include_hidden=True`` prints all links
in the navigatio menu.

-----------
Limitations
-----------

I created this theme with manually written "prose" documentation in mind. There are no
styles provided for API documentation yet. There may be styles missing for some roles or
directives that I am not typically using. This version of the theme only really supports
English as a language.

.. include-until-here

-------------
Documentation
-------------

Read the documentation and see how the theme looks over there.
