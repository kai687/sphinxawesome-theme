Admonitions
===========

This page shows the available admonitions for this theme.

Tips
----

Tips are positive admonitions. A tip can be a shortcut for an action that was further
explained in the main text, or a confirmation.

.. tip::

   This is how a tip appears.

The ``hint`` admonition is considered equivalent and appears in the same style.

Notes
-----

Notes are neutral admonitions, that can draw the attention of the reader, but usually
don't have a positive or negative effect.

.. note::

   This is how a note appears.

If you want to include a list of references to further documentation, you can use the
``seealso`` directive.

.. seealso::

   `Sphinx directives <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_,
   `Docutils directives <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_

Use a general admonition for notes with custom titles.

.. admonition:: How to give the admonition a title?

   Provide the title directly after the directive, for example,

   .. code-block:: rst

      .. admonition:: How to give the admonition a title?

Caution
-------

Use a ``caution`` admonition to make the user aware of important issues, or
consequences.

.. caution::

   This is how a caution appears.

The ``important`` admonition is considered equivalent and appears in the same style.

Warning
-------

A ``warning`` is a negative admonition. Typically, anything involving security should
be emphasized with a warning. Ignoring the information in a warning usually has
negative consequences.

.. warning::

   This is how a warning appears.

The ``danger`` and ``error`` admonitions are considered equivalent and appear in the
same style.

Block quotations
----------------

.. vale off

Block quotations aren't admonitions, but are used to quote other material and as such
are often set apart from the main text.

    "It is my business to know things. That is my trade."

    -- Sherlock Holmes
