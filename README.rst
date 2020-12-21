Sphinx awesome theme
====================

.. image:: https://img.shields.io/pypi/l/sphinxawesome-theme?color=blue
   :target: https://opensource.org/licenses/MIT
   :alt: MIT license

.. image:: https://img.shields.io/pypi/v/sphinxawesome-theme
   :target: https://pypi.org/project/sphinxawesome-theme
   :alt: PyPI package version number

.. image:: https://api.netlify.com/api/v1/badges/e6d20a5c-b49e-4ebc-80f6-59fde8f24e22/deploy-status
   :target: https://app.netlify.com/sites/sphinxawesome-theme/deploys
   :alt: Netlify Status

.. readme-start

This is an awesome theme and a set of extensions
for the Sphinx_ documentation generator.
Using this theme and extension,
you can change the look of your documentation website
and add a number of useful improvements.
See the theme in action at https://sphinxawesome.xyz.

.. _Sphinx: http://www.sphinx-doc.org/en/master/

Getting started
---------------

You can install the awesome theme from the Python package index
and modify the Sphinx configuration file ``conf.py``.

To get started using this theme, follow these steps:

#. Install the theme as a Python package.

   .. code:: console

      $ pip install sphinxawesome-theme


   See `How to install the theme`_ for more information.

   .. _How to install the theme: https://sphinxawesome.xyz/how-to/install

#. Add the ``html_theme`` configuration option
   to the Sphinx configuration file ``conf.py``.

   .. code:: python

      html_theme = "sphinxawesome_theme"

   See `How to use the theme`_ for more information.

   .. _How to use the theme: https://sphinxawesome.xyz/how-to/use

Features
--------

This theme is designed with readability and usability in mind.
The theme includes several extensions that enhance the usability:

Awesome code blocks
    - Code blocks have a header section, displaying the optional caption,
      as well as the programming language used for syntax highlighting
    - The code block headers contain a **Copy** button, allowing you to copy
      code snippets to the clipboard.
    - The theme adds two new options to Sphinx's ``code-block`` directive:
      ``emphasize-added`` and ``emphasize-removed``, allowing you to highlight
      code changes within other highlighted code.

Awesome new directive for highlighting placeholder variables
    The theme supports a new directive ``samp``, which is the equivalent of the
    built-in ``:samp:`` interpreted text role. This allows you to highlight placeholder
    variables in code blocks.

Awesome user experience improvements
    These small features make the theme more usable. To name a few:
    
    - better keyboard navigation:
    
      - use the ``Tab`` key to navigate through all sections on the page
      - use the *Skip to Content* link to bypass the navigation links
      - use the ``/`` key (forward Slash) to focus the search input element
      
    - better “permalink” mechanism:
    
      - hovering over an element with a permalink reveals a *Link* icon
      - selecting the *Link* icon copies the link to the clipboard
      - notes, warnings and other admonitions have permalinks by default
      
    - collapsible elements: 
    
      - nested navigation links – all pages are reachable from all other pages
      - code definitions – code object definitions (functions, classes, modules, etc.), for example obtained via the ``sphinx.ext.autodoc`` extension.
