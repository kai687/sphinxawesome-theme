.. meta::
   :description: See how on-page navigation looks like in this theme.
   :twitter:description: See how on-page navigation looks like in this theme.

On-page navigation
==================

.. rst-class:: lead

   When you have many sections on a page, you can provide
   a table of contents for a better overview.

----

To show a table of contents for the current page,
use the ``contents`` directive with the ``:local:`` option.
You must provide a title to the directive, or it won't show.
By default, headings included after this directive are links back to the contents section.
If you want to turn off this behavior, use ``:backlinks: none``.

.. code-block:: rst

   .. contents:: On this page
      :local:
      :backlinks: none

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
