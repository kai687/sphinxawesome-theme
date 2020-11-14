First, test an implicit code block.
Those should be highlighted with language "python".

::

   print("Hello")

Now, check an explicit label before a code block.

.. _foo:

::

   print("Hello")

Next, test a code block with a caption

.. code-block:: python
   :caption: test

   print("Hello")

Next, test a code block with a caption and an explicit label.

.. _bar:

.. code-block:: python
   :caption: test

   print("Hello")

Now, test a code block showing line numbers

.. code-block:: python
   :linenos:

   print("Hello")

Now, test a code block with a highlighted line

.. code-block:: python
   :emphasize-lines: 1

   print("Hello")

Now, test a code block with added/removed lines

.. code-block:: python
   :emphasize-added: 1
   :emphasize-removed: 2

   print("Added")
   print("Removed")

Test a non-literal container (for coverage)

.. container:: bogus

   Doesn't do much.

.. parsed-literal::

   *Markup*
