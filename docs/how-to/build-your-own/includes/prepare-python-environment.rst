.. _sec:install-python-deps:

Prepare Python environment
--------------------------

The |product| uses these Python tools:

- Poetry_ to manage the Python dependencies and building the package
- Nox_ to test and lint the Python code, and to build the docs
- Pipx_ to install Python applications in isolated environments and making them available globally

.. _Poetry: https://python-poetry.org/
.. _Nox: https://nox.thea.codes/en/stable/
.. _Pipx: https://pypa.github.io/pipx/

If you want to use the same versions of the Python tools,
you can provide a :gh:`requirements.txt <requirements.txt>` to the install commands.

To prepare the Python environment, run these commands:

.. code-block:: terminal

   pip install --user pipx [--requirement=requirements.txt]
   pipx install poetry [--pip-args=--requirement=requirements.txt]
   pipx install nox [--pip-args=--requirement=requirements.txt]
