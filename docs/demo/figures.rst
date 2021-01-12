Figures and tables
==================

On this page, styles for figures and tables are shown.

Images
------

For simple images without captions, use the ``image`` directive.

.. image:: image.svg
   :alt: A placeholder image

Use the ``:align: center`` option to center an image.

.. image:: image.svg
   :width: 50%
   :alt: A centered placeholder image
   :align: center

Use ``:align: right`` option to align the image to the right edge.

.. image:: image.svg
   :width: 50%
   :alt: A right-aligned placeholder image
   :align: right

Figures
-------

If you want to add captions and legends to the image, use the ``figure`` directive.

.. figure:: image.svg
   :alt: A grey placeholder image

   This is an image caption.

   And you can also provide a legend to the figure that contains more information about
   the image.


You can control the image alignment by using the `:align:` option.


.. figure:: image.svg
   :alt: A centered placeholder image in figure environment
   :width: 50%
   :align: center

   Use ``:align: center`` to center a figure.



.. figure:: image.svg
   :width: 50%
   :alt: A right-aligned placeholder image in figure environment
   :align: right

   Use ``:align: right`` to right-align a figure.


Tables
------

This is a small table.

.. table:: Table caption
   :width: 100%

   ==========  ==========
   table head  table head
   ==========  ==========
   column      column
   column      column
   column      column
   ==========  ==========
