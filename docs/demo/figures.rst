.. meta::
   :description: Discover how the theme styles figures, images, and their supporting elements, such as captions.
   :twitter:description: Discover how the theme styles figures, images, and their supporting elements, such as captions.

Figures and tables
==================

.. rst-class:: lead

   See how images, figures, and tables look like with the |product|.
   Sphinx distinguishes between *images* and *figures*.

Images
------

For images without captions or legends, use the ``image`` directive.

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

   You can also provide a legend to the figure with the ``:legend:`` option.
   The images on this page are from https://undraw.co/.


You can control the image alignment by using the ``:align:`` option.


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
