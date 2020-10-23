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
   :emphasize-added: 3
   :emphasize-removed: 4
   :emphasize-lines: 6

   def function(greet: str, name: str) -> str:
      """Some test function."""
      tmp = 5
      tmp = 10
      tmp = 15
      return f"{greet} {name}!"
