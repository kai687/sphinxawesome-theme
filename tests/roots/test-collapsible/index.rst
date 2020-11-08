Test
====

This document tests autodoc like "definition lists" for code objects.

First, let's check a default definition list that should always remain
uncollapsible.

term
   definition


Next, test a command line option. If the option ``html_collapsible_definitions``
is on, this should be collapsible (although in these tests we only test if
the classes are correctly applied. Visual testing needs to confirm if it is
actually collapsible or not.)

.. option:: -t

   test
