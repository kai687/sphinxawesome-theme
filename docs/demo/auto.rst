.. meta::
   :description: See an example for module documentation with the Awesome theme. Sphinx generates module documentation from docstrings in the source code.

Module documentation
====================

.. rst-class:: lead

   See how automatically generated documentation from Python source code
   looks like with the |product|.

.. vale Vale.Spelling = NO

Automodule example
------------------

.. vale Vale.Spelling = YES

.. automodule:: docutils
   :members:

.. vale Vale.Spelling = NO

Autoclass example
-----------------

.. vale Vale.Spelling = YES

.. autoclass:: docutils.nodes.Node
   :members: walk

.. vale Vale.Spelling = NO

Autofunction example
--------------------

.. vale Vale.Spelling = YES

.. autofunction:: docutils.nodes.serial_escape

Command line options
--------------------

If you want to document command-line options, you have two choices:

- The ``option`` directive (Sphinx)
- An option list (docutils)

Option directive
~~~~~~~~~~~~~~~~

Sphinx comes with the ``option`` directive. This renders every option
into its own element, including permalinks:

.. option:: -h, --help

   Display a (hopefully) useful message.

.. option:: -i FILE, --input FILE

   Specify an input file.

.. option:: -v, --verbose

   Increase the verbosity.

Option lists
~~~~~~~~~~~~

A compact way to display command-line options is built into the ``docutils`` module and works in Sphinx too:

-h, --help              Display a helpful message.
-i FILE, --input FILE   Specify an input file.
-v, --verbose           Increase the verbosity.
