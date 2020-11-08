On-page navigation
==================

Use a ``toctree`` directive without the ``:hidden:`` option to include
a table of contents on the same page.


.. toctree::
   :caption: Other pages
   :maxdepth: 1

   ../about
   ../glossary


For displaying only content of the current page, use the ``contents``
directive with the ``:local:`` option. You must provide a title for the
directive to render. It'll silently fail to render otherwise. By default,
headings after this directive will be links back to the contents section
(such as on this page). If you want to disable this behavior,
use ``:backlinks: none``.

.. contents:: On this page
   :local:


Section 1
---------

Some random text.

Subsection 1.1
~~~~~~~~~~~~~~

More random text

Subsection 1.2
~~~~~~~~~~~~~~

More random text

Section 2
---------
Some random text.

Subsection 2.1
~~~~~~~~~~~~~~

More random text

Subsection 2.2
~~~~~~~~~~~~~~

More random text
