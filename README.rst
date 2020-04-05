Library Template (libtemplate)
==============================

``libtemplate`` (short for 'Library Template') is a Python library that should
be used as a template to build one's own library, as the name suggests. In this
file you should provide a brief description of whatever library you decide to
create out of this template.

Note #1: restructuredText
-------------------------

This README file is an .rst file, which uses restructuredText_: an
easy-to-read markup syntax and parser system. Whether one is writing
documentation files, or Python source code, it is good practice to keep all
lines of text no longer than 80 characters. There are different ways of
ensuring this. For emacs users, one can use the fill-column-indicator_ package.

Note #2: Files to leave unchanged
---------------------------------

Here is a list of files and directories that you do not need to change:

- requirements-doc.txt
- setup.py
- docs/Makefile
- docs/make.bat
- docs/index.rst
- docs/conf.py
- docs/changelog.rst
- docs/_templates

Note #3: Use PEP 8 as a style guide
-----------------------------------

 It is a good idea to try and follow the coding conventions laid out in
 `PEP 8`_.

Note #4: Copy ``libtemplate`` repo to start your own library
------------------------------------------------------------

To start your own library using ``libtemplate`` as the template, open up the
file ``gencopy.py`` in the root directory of the ``libtemplate`` repository,
edit the variables ``new_lib_name``, ``author_name``, ``copyright_year``,
``email``, and ``lib_description``, and then run the script::

    python gencopy.py

The script will copy the ``libtemplate`` repository into a new directory up one
level from the root of the ``libtemplate`` repository. The new directory will
have the same name as that specified in the variable ``new_lib_name``. Moreover,
the script will replace all library name, author name, copyright year, email,
and library description placeholders by the strings stored in ``new_lib_name``,
``author_name``, ``copyright_year``, ``email``, and ``lib_description``
respectively. The only exception is that the library name is not replaced in
any of the files stored in the directory ``libtemplate`` (relative to the
repository root), or the files ``README.rst`` and ``INSTALL.rst``.

.. _restructuredText: https://docutils.sourceforge.io/rst.html
.. _fill-column-indicator: https://www.emacswiki.org/emacs/FillColumnIndicator
.. _PEP 8: https://www.python.org/dev/peps/pep-0008/
