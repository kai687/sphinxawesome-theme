====================
Sphinx awesome theme
====================
   
.. image:: https://img.shields.io/pypi/l/sphinxawesome-theme?color=blue&style=for-the-badge
   :target: https://opensource.org/licenses/MIT
   :alt: MIT license
   :class: badge
   
.. image:: https://img.shields.io/pypi/v/sphinxawesome-theme?style=for-the-badge
   :target: https://pypi.org/project/sphinxawesome-theme
   :alt: PyPI package version number
   :class: badge

.. image:: https://img.shields.io/netlify/e6d20a5c-b49e-4ebc-80f6-59fde8f24e22?style=for-the-badge
   :target: https://sphinxawesome.xyz
   :alt: Netlify Status
   :class: badge

This is a simple but awesome theme for the `Sphinx
<http://www.sphinx-doc.org/en/master/>`_ documentation generator.


------------
Installation
------------

.. install-start

Install the theme as a Python package:

.. code:: console

   pip install sphinxawesome-theme

.. install-end

-----
Usage
-----

.. use-start

To use the theme, set ``html_theme`` in the Sphinx configuration file
``conf.py``:

.. code:: python

   html_theme = "sphinxawesome_theme"

To include all entries in the navigation menu, add the following setting to the Sphinx
configuration file ``conf.py``.

.. code:: python

   html_theme_options = {"nav_include_hidden": True}

If you set the option ``:hidden:`` to a toctree_ directive, the content will be
included, but the list of links to the documents will not be written on the page itself.
This can be useful when navigation links are shown elsewhere.

.. _toctree: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree

The Sphinx awesome theme shows a navigation menu on the left side of all pages, so
having the links shown in the content area is not necessary. In order allow an easy
transition from other Sphinx themes, the default is ``nav_include_hidden = False``.

To make best use of this theme, include the ``:hidden:`` option to all ``..toctree``
directives and set ``nav_include_hidden = True``.

.. use-end

----
Demo
----

See how the theme looks on the `demo page <https://sphinxawesome.xyz>`_.
