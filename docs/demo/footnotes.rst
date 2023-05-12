.. meta::
   :description: See how footnotes are styled in the Awesome theme.
   :twitter:description: See how footnotes are styled in the Awesome theme.

Footnotes
=========

.. rst-class:: lead

   Footnotes are a way in printed documents to add more information outside of the main
   flow of text.

----

Footnotes don't apply well to online experiences,
especially to mobile screens.

.. [1] To create a footnote, create a label and indent it by three spaces.

   .. code-block:: rst

      .. [1] To create a footnote, create a label and indent it by three spaces.

.. [#label] As footnote labels, you can use numbers [1]_, labels [#label]_,
   or you can use automatic labeling [#]_

   .. code-block:: rst

      .. [#label]_ As footnote labels, you can use numbers [1]_, labels [#label]_,
         or you can use automatic labeling [#]_.

.. [#] An automatically numbered footnote. You can also use hyperlinks to the footnote
   labels: label_.
