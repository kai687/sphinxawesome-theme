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
directive with the ``:local:`` option.

.. contents:: On this page
   :local:
   :backlinks: none


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
