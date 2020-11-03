===========
Admonitions
===========

Admonitions can provide additional explanations, or caution the user before proceeding
with the next step. Sphinx and the underlying docutils module define a large number of
admonitions. Since many of them are overlapping in their intended meaning, any project
should only need a few.

----
Tips
----

Tips are positive admonitions.
A tip can be a shortcut for an action that was just explained,
or a confirmation,
that users are on the right path.

.. tip::

   This is how a tip appears.

The ``hint`` admonition is considered equivalent and appears in the same style.

-----
Notes
-----

Notes are neutral admonitions, that can draw the attention of the reader, but usually
don't have a positive or negative effect.

.. note::

   This is how a note appears.

If you want to include a list of references to further documentation, you can use the
``seealso`` directive.

.. seealso:: `Sphinx directives
   <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_, `Docutils directives <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_

Use a general admonition for notes with custom titles.

.. admonition:: How to give the admonition a title?

   Provide the title directly after the directive, for example,

   .. code-block:: rst

      .. admonition:: How to give the admonition a title?

-------
Caution
-------

A ``caution`` should be used, when the user **should** be aware of something before
moving on. As a negative admonition, ignoring it might have unwanted consequences,
although not as detrimental that would warrant a warning.

.. caution::

   This is how a caution appears.

The ``important`` admonition is considered equivalent and appears in the same style.

-------
Warning
-------

A ``warning`` is a strong, negative admonition. Typically, anything involving
security should be emphasized with a warning. Ignoring the information in a warning
usually has negative consequences.

.. warning::

   This is how a warning appears.

The ``danger`` and ``error`` admonitions are considered equivalent and appear in
the same style.

-----------
Blockquotes
-----------

Blockquotes are not really admonitions, but are used to quote other material and as such
are often set apart from the main text.

    "It is my business to know things. That is my trade."

    -- Sherlock Holmes
