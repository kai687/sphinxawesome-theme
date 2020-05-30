=========================
Code, figures, and tables
=========================

----
Code
----

This theme adds a :guilabel:`Copy` button to code blocks. Clicking on the button will
copy the text inside the code block to the clipboard.

.. parsed-literal::

   Parsed literal blocks *can* contain reStructuredText!
   But they don't have syntax highlighting


.. code-block:: python
   :emphasize-lines: 2
   :linenos:

   print("Don't highlight this")
   print("But this!")
   print("And this is unimportant again")


-------
Figures
-------

.. figure:: image.svg
   :alt: A grey placeholder image

   This is an image caption.

   And you can also provide a legend to the figure that contains more information about
   the image.

------
Tables
------

This is a small table.

.. table:: Table caption
   :width: 66%

   ==========  ==========
   table head  table head
   ==========  ==========
   column      column
   column      column
   column      column
   ==========  ==========
