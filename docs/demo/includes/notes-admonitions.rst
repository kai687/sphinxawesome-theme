Tips
----

Use the :dir:`tip` directive to highlight information that has a positive effect for users.
For example, a tip can be a shortcut or a confirmation.

.. tip::

   This is how a tip appears.

You can also use the :dir:`hint` directive,
which appears in the same style.

.. hint::

   Hints and tips appear in the same style.

Notes
-----

Use the :dir:`note` directive to provide extra information.

.. note::

   This is how a note appears.

To include a list of references, you can use the :dir:`seealso` directive.

.. seealso::

   :sphinxdocs:`Sphinx directives <usage/restructuredtext/directives.html>`
   `Docutils directives <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_


To create notes with custom titles, use the :dir:`admonition` directive:

.. code-block:: rst

   .. admonition:: How to give a note a custom title?

      Enter the custom title after after the :rst:dir:`admonition` directive.

This renders as:

.. admonition:: How to give a note a custom title?

   Enter the custom title after the :dir:`admonition` directive.

Cautions
--------

Use a :dir:`caution` directive to alert users about important issues.

.. caution::

   This is how a caution appears.

You can also use the :dir:`important` directive, which appears in the same style.

.. important::

   Important and caution callouts appear in the same style.

As does the :dir:`warning` directive.

.. warning::

   This is a warning.

And the :dir:`attention` directive.

.. attention::

   Makes you wonder what the semantic difference between all those callouts are.

Errors
------

You can use the :dir:`error` directive to inform users about errors..

.. error::

   This is how a warning appears.

You can also use the :dir:`danger` directive, which appears in the same style.

.. danger::

   This is how a potentially dangerous step appears.
