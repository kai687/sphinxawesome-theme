=========================
This is a code test file
=========================

This is a regular old paragraph with some ``inline code``.

::

   # should be in python
   print("Hello World")

.. parsed-literal::

   *This* should be parsed, but not highlighted!!!


.. code-block:: javascript

   console.log("Look at the header!")


.. code-block:: python
   :caption: Codeblock with caption!

   def function(greet: str, name: str) -> str:
      """Some test function."""
      return f"{greet} {name}!"
