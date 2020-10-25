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

Awesome code blocks
    - Code blocks have a **Copy** button, allowing you to copy code snippets to the
      clipboard. They also show the programming language of the code block.
    - Sphinx's ``code-block`` directives are enhanced with ``emphasize-added`` and
      ``emphasize-removed`` options for highlighting added and removed lines.

Awesome new directive for highlighting placeholder variables
    The theme supports a new directive ``samp``, which is the equivalent of the
    built-in ``:samp:`` interpreted text role. This allows you to highlight placeholder
    variables in code blocks.

Awesome user experience improvements
    A lot of small features make the theme more usable. To name a few:

    - Use the **Tab** key to navigate through all sections of the page. Every page has a
      *Skip to Content* link to bypass navigation links.
    - Link to notes, warnings, etc. Their titles have IDs and use the same “permalink”
      mechanism as headings and other captions.
    - Better “permalink” mechanism. Hovering over an element with a permalink reveals a
      *Link* icon.  Select the *Link* icon to copy the link to the clipboard.
    - Collapsible navigation menu: All pages are reachable from all other pages.
    - CSS tooltips. Provide more accessible information compared to the ``title``
      attribute which only works for mouse users.
    - Press the ``/`` (Slash) key to focus the search input and start searching.

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
