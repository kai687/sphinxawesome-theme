=========================
This is a sample document
=========================


This is a regular paragraph with some ``inline code``.


::

   # although it should be highlighted with Python
   This is a literal block without any special meaning

::

   # this should be python
   print("Hello world!")

.. parsed-literal::

   And *this* is a parsed literal block with ReST in it!


.. parsed-literal::

   Now what really happens, if I have a super-duper long line. I'm mostly curious about the line break.

.. code-block:: python

   def function(greet: str, name: str) -> str:
      """Some test function."""
      return f"{greet} {name}!"

.. code-block:: python
   :caption: Codeblock with caption!

   def function(greet: str, name: str) -> str:
      """Some test function."""
      return f"{greet} {name}!"


.. code:: python

   print("Hello code directive from docutils.")


.. code-block::

   print("This is a super extremely long line. Will it break correctly, I wonder. I'm mostly interested in the overflow properties of these nested elements.")
