Tabs
----

This is a tab.

.. tab-set::

    .. tab-item:: Tab 1

       This is some tab content.
       We want to render a little more.
       Ideally with a linebreak to get the full width.

       .. code-block:: js

          console.log("A code block in a tab.")

    .. tab-item:: Tab 2

       Short lines should still be full width.
       They aren't!

Tabs are often used for code elements.
Add the `no-header` classes to code blocks to make them look better in tabs.


.. tab-set-code::

   .. code-block:: python
      :class: no-header

      print("Hello world from a tab.")

   .. code-block:: js
      :class: no-header

      console.log("Hello world from a tab.")

   .. code-block:: ruby
      :class: no-header

      puts 'Hello world from a tab.'
