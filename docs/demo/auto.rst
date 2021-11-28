.. meta::
   :description: See an example how module documentation looks like with this theme. Sphinx generates module documentation from docstrings in the source code.


====================
Module documentation
====================

On this page, you'll see an example how automatically generated
module documentation looks like in Sphinx.


.. vale Awesome.SpellCheck = NO

------------------
Automodule example
------------------

.. vale Awesome.SpellCheck = YES

.. automodule:: docutils
   :members:

.. vale Awesome.SpellCheck = NO

-----------------
Autoclass example
-----------------

.. vale Awesome.SpellCheck = YES

.. autoclass:: docutils.nodes.Node
   :members: walk

.. vale Awesome.SpellCheck = NO

--------------------
Autofunction example
--------------------

.. vale Awesome.SpellCheck = YES

.. autofunction:: docutils.nodes.serial_escape


--------------------
Command line options
--------------------

If you want to document command-line options, you have two choices.
Sphinx comes with the ``option`` directive. This renders every option
into its own element, including links:

.. option:: -h, --help

   Display a (hopefully) useful message.

.. option:: -i FILE, --input FILE

   Specify an input file.

.. option:: -v, --verbose

   Increase the verbosity.


------------
Option lists
------------

A more compact way is built into the ``docutils`` module and works in Sphinx too:

-h, --help              Display a helpful message.
-i FILE, --input FILE   Specify an input file.
-v, --verbose           Increase the verbosity.
