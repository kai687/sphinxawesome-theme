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

This is an awesome theme for the Sphinx_ documentation generator.
See how the theme looks on the `demo page`_.

.. _Sphinx: http://www.sphinx-doc.org/en/master/
.. _demo page: https://sphinxawesome.xyz


--------
Features
--------

The theme includes several usability improvements:

.. features-start

Better code blocks
    - Code blocks have a **Copy** button, allowing you to copy code snippets to the
      clipboard.
    - Code blocks are enhanced with ``emphasize-added`` and ``emphasize-removed``
      options, that highlight removed lines in red and added lines in green.

New directive for highlighting placeholder variables
    The theme supports a new directive ``samp``, which is the equivalent of the
    built-in ``:samp:`` interpreted text role. This allows you to highlight placeholder
    variables in code blocks.

Improved user experience
    A lot of small features make the theme more usable. To name a few:

    - You can tab through headlines and captions enabling easy navigation with the
      keyboard.
    - You can link to admonitions. Their titles have the same “permalink” mechanism as
      headlines and captions.
    - Clicking on the ``#`` icon for permalinks copies the link to the clipboard.
    - Collapsible navigation menu: All elements are reachable from all pages.
    - Keyboard shortcut for the search input: ``/``.

.. features-end

------------
Installation
------------

Install the theme as a Python package:

.. install-start

.. code:: console

   $ pip install sphinxawesome-theme

.. install-end

Read the full `installation instructions`_ for more information.

.. _installation instructions: https://sphinxawesome.xyz/docs/install/#how-to-install-the-theme

-----
Usage
-----

.. use-start

To use the theme, set the ``html_theme`` configuration setting
in the Sphinx configuration file ``conf.py``:

.. code:: python

   html_theme = "sphinxawesome_theme"

.. use-end

Read the full `usage information`_ for more information.

.. _usage information: https://sphinxawesome.xyz/docs/use/#how-to-use-the-theme
