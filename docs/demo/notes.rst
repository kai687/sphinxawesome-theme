.. meta::
   :description: Notes and warnings allow you to draw attention to issues or provide extra information. See how they look like with this theme.

Notes, warnings, and quotations
===============================

.. rst-class:: lead

   You can use one of the following directives to mark up **additional information**.
   These elements are often called *admonitions* or *call-outs*.

----

Tips
----

You can use the ``tip`` directive to highlight information that has a positive effect
for the user. For example, a tip can be a shortcut or a confirmation.

.. tip::

   This is how a tip appears.

You can also use the ``hint`` element, which appears in the same style.

.. hint::

   Hints and tips appear in the same style.

Notes
-----

You can use the ``note`` directive to provide extra information.

.. note::

   This is how a note appears.

To include a list of references, you can use the ``seealso`` directive.

.. seealso::

   :sphinxdocs:`Sphinx directives <usage/restructuredtext/directives.html>`
   `Docutils directives <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_


You can also create notes with custom titles. Use the ``admonition`` directive:

.. code-block:: rst

   .. admonition:: How to give a note a custom title?

      Enter the custom title after after the ``admonition`` directive.

This gets rendered as:

.. admonition:: How to give a note a custom title?

   Enter the custom title after the ``admonition`` directive.

Cautions
--------

You can use a ``caution`` directive to alert the user about important issues.

.. caution::

   This is how a caution appears.

You can also use the ``important`` directive, which appears in the same style.

.. important::

   Important and caution call-outs appear in the same style.

Warnings
--------

You can use the ``warning`` directive to warn the user about negative consequences.
For example, anything involving security should be emphasized with a warning.

.. warning::

   This is how a warning appears.

You can also use the ``danger`` and ``error`` directives, which appear in the same
style.

.. danger::

   This is how a potentially dangerous step appears.

.. warning::

   This is how a warning appears.


Block quotations
----------------

.. vale off

You can use block quotations to highlight quotes.


    "It is my business to know things. That is my trade."

    -- Sherlock Holmes
