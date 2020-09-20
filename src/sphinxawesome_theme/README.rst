Jinja2 templates and Python code
--------------------------------

This directory contains the Jinja2_ templates,
that are interpolated by Sphinx when building
the website.

.. _Jinja2: https://jinja.palletsprojects.com/en/2.11.x/

The main templates is ``layout.html``. This file
contains the overall structure and imports
further template files for components, like the
header (``header.html``) or the navigation menu (``nav.html``).

The directory also contains some Python modules,
that modify aspects of Sphinx. The main entry entry
point is ``__init__.py``.

``admonitions_ids.py``
   The transform defined in this file adds unique identifiers
   to ``admonition`` nodes, so that they become link targets
   as well—Sphinx by default does not allow linking to Notes,
   Warnings, etc.

``html_translator.py``
   The methods in this file override default Sphinx behavior,
   when transforming into HTML5. Mostly, the titles of the
   headerlinks are changed to be a little more semantic.
   The default text *Permalink to this section* isn't all that useful.
   It's a lot of code for something so small, but I wanted
   this to happen at build time, not at runtime in JavaScript
   like I had it at the beginning.

``highlighting.py``
   Implements the ability to highlight added and removed lines
   in Pygments_, and exposes these options in Sphinx's
   ``code-block`` directive.

``jinja_filter.py``
   Provides a simple filter ``sanitize`` that takes a string
   and transforms it to an ID, that can be used for linking.
   This is currently only used in the ``skip.html`` link,
   but I wanted an example for how-to provide custom filters.

``postprocess.py``
   Implements several functions to postprocess the HTML after
   the build finished. This mostly deals with quirks of the
   HTML that comes from docutils and Sphinx (mostly docutils).
   While the optimal way to deal with them would be during
   build time, I would practically have to re-implement a bulk
   of the HTML5 writer from docutils.
   For example, useless wrapping of elements and easy targets
   to make the HTML more semantic, for example I prefer using
   ``<section>`` elements over ``<div class="section">``. I say
   easy targets, because there's potential for a whole lot of more,
   which I will have to leave untapped for the time being.

.. _Pygments: https://pygments.org/
