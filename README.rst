====================
Sphinx Awesome Theme
====================
   
.. image:: https://img.shields.io/pypi/l/sphinxawesome-theme?color=blue&style=for-the-badge
   :target: https://opensource.org/licenses/MIT
   :alt: MIT license
   
.. image:: https://img.shields.io/pypi/v/sphinxawesome-theme?style=for-the-badge
   :target: https://pypi.org/project/sphinxawesome-theme
   :alt: PyPI package version number

.. image:: https://api.netlify.com/api/v1/badges/e6d20a5c-b49e-4ebc-80f6-59fde8f24e22/deploy-status
   :target: https://app.netlify.com/sites/confident-austin-7d4cfd/deploys
   :alt: Netlify Status

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
not print the list of links to the documents on the current page. This is useful when
navigation links are shown elsewhere, for example in a menu on the left side. The
default is ``nav_include_hidden=False`` in order to be compatible with other themes.

-----------
Limitations
-----------

This theme is designed to be simple. Some features are not (or not yet) available.

- Zero customizability
- API documentation has not been tested. Some styles are missing. 
- Not all docutils/Sphinx roles have styles. There are a lot of them. 
- Internationalization was neglected.

.. include-until-here

-------------
Documentation
-------------

Read the documentation and see how the theme looks on the `demo page
<https://sphinxawesome.xyz>`_
