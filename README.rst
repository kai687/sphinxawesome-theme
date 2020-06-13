====================
Sphinx awesome theme
====================
   
.. image:: https://img.shields.io/pypi/l/sphinxawesome-theme?color=blue&style=for-the-badge
   :target: https://opensource.org/licenses/MIT
   :alt: MIT license
   
.. image:: https://img.shields.io/pypi/v/sphinxawesome-theme?style=for-the-badge
   :target: https://pypi.org/project/sphinxawesome-theme
   :alt: PyPI package version number

.. image:: https://img.shields.io/netlify/e6d20a5c-b49e-4ebc-80f6-59fde8f24e22?style=for-the-badge
   :target: https://sphinxawesome.xyz
   :alt: Netlify Status

This is an awesome theme for the `Sphinx
<http://www.sphinx-doc.org/en/master/>`_ documentation generator. See how the theme
looks on the `demo page <https://sphinxawesome.xyz>`_.


--------
Features
--------

.. features-start

The theme includes several usability improvements:

Copy code blocks
    Code blocks have a **Copy** button, that allows you to copy code snippets to the
    clipboard.

Improved links after headlines and captions
    Clicking on the ``#`` character that appears when hovering over headlines and
    captions copies that link to the clipboard. The tooltips for links after headlines
    also show the section title, instead of the generic "Permalink to this headline".

New directive for highlighting placeholder variables
    The theme supports a new directive ``samp``, which is the equivalent of the
    built-in ``:samp:`` interpreted text role. This allows you to highlight placeholder
    variables in code blocks.

.. features-end

------------
Installation
------------

Install the theme as a Python package:

.. install-start

.. code:: console

   $ pip install sphinxawesome-theme

.. install-end

Read the full `installation instructions
<https://sphinxawesome.xyz/docs/install.html#how-to-install-the-theme>`_ for more
information.

-----
Usage
-----

.. use-start

To use the theme, set ``html_theme`` in the Sphinx configuration file
``conf.py``:

.. code:: python

   html_theme = "sphinxawesome_theme"

.. use-end

Read the full `usage guide
<https://sphinxawesome.xyz/docs/use.html#how-to-use-the-theme>`_ for more information.
