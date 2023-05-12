Tips
----

Use the ``tip`` directive to highlight information that has a positive effect for users.
For example, a tip can be a shortcut or a confirmation.

.. tip::

   This is how a tip appears.

You can also use the ``hint`` directive,
which appears in the same style.

.. hint::

   Hints and tips appear in the same style.

Topic
-----

.. caution::

  :octicon:`alert;1em;sd-text-warning`
  The |product| doesn't include styles for the ``topic`` directive.
  Use a block quotation or another alert type instead.

Notes
-----

Use the ``note`` directive to provide extra information.

.. note::

   This is how a note appears.

To include a list of references, you can use the ``seealso`` directive.

.. seealso::

   :sphinxdocs:`Sphinx directives <usage/restructuredtext/directives.html>`
   `Docutils directives <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_


To create notes with custom titles, use the ``admonition`` directive:

.. code-block:: rst

   .. admonition:: How to give a note a custom title?

      Enter the custom title after after the ``admonition`` directive.

This renders as:

.. admonition:: How to give a note a custom title?

   Enter the custom title after the ``admonition`` directive.

Warnings
--------

Use a ``warning`` directive to alert users about important issues.

.. warning::

   This is a warning.

You can also use the ``important``, ``attention``, or ``caution`` directives, which appear in the same style.

.. caution::

   This is how a caution appears.

.. important::

   Important and caution callouts appear in the same style.

.. attention::

   Makes you wonder what the semantic difference between all those callouts are.

Errors
------

You can use the ``error`` directive to inform users about errors..

.. error::

   This is how an error appears.

You can also use the ``danger`` directive, which appears in the same style.

.. danger::

   This is how a potentially dangerous step appears.
