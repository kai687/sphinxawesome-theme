=========================
This is a sample document
=========================


This is a regular paragraph with some ``inline code``.


::

   This is a literal block without any special meaning


::

   # this should be python
   print("Hello world!")


.. parsed-literal::

   And *this* is a parsed literal block with ReST in it!


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
