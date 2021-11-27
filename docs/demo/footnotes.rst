.. meta::
   :description: See how footnotes are styled in the Awesome theme.

Footnotes
=========

.. rst-class:: lead

   Footnotes are another way of putting information outside of the main text.
   They're a concept from print writing that doesn't apply well to online media,
   especially on mobile devices. If you're creating a documentation website,
   consider not using footnotes at all.

----

.. [1] To create a footnote, create a label and indent it by three spaces.

   .. code-block:: rst

      .. [1] To use a footnote...

.. [#label] As footnote labels, you can use numbers [1]_, labels [#label]_,
   or you can use automatic labeling [#]_

   .. code-block:: rst

      .. [#label]_ As footnote labels, you can use numbers [1]_, labels [#label]_,
         or you can use automatic labeling [#]_.

.. [#] An automatically numbered footnote. You can also use hyperlinks to the footnote
   labels: label_.
