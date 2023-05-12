.. meta::
   :description: See an example for code documentation with the Awesome theme. Sphinx can generate reference documentation from docstrings in your source code.
   :twitter:description: See an example for code documentation with the Awesome theme. Sphinx can generate reference documentation from docstrings in your source code.

Code documentation
==================

.. rst-class:: lead

   Sphinx can generate reference documentation from docstrings in your source code.


The |product| documentation makes use of this function on the page :ref:`sec:theme-options`.
This page lists a few additional examples for command line options.

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
