# Library Template (libtemplate)

`libtemplate` (short for 'Library Template') is a Python library that should be
used as a template to build one's own library, as the name suggests. In this
file you should provide a brief description of whatever library you decide to
create out of this template.

## Note #1: Files to leave unchanged

Here is a list of files and directories that you do not need to change:

* requirements-doc.txt
* .gitlab-ci.yml (if generated)
* docs/Makefile
* docs/make.bat
* docs/api.rst
* docs/index.html (if generated)
* docs/.nojekyll (if generated)
* docs/changelog.rst
* docs/_static/readthedocs-custom.css
* docs/_templates

## Note #2: Recommended coding conventions

It is a good idea to try and follow the coding conventions laid out in
[PEP 8](https://www.python.org/dev/peps/pep-0008/).

Moreover, it is good practice to keep all lines of text/code no longer than 80
characters. There are different ways of ensuring this. For emacs users, one can
use the
[fill-column-indicator](https://www.emacswiki.org/emacs/FillColumnIndicator)
package.

## Note #3: Copy `libtemplate` repo to start your own library

To start your own library using `libtemplate` as the template, copy the file
`<root>/gencopy_template.py` to `<root>/gencopy.py`, where `<root>` is the root
of the `libtemplate` repository. Then open up the file `<root>/gencopy.py`; edit
the variables `new_lib_name_for_imports`, `new_lib_name_for_docs`,
`author_name`, `copyright_year`, `email`, `lib_description`,
`path_to_new_repo_root`, and `target_git_platform`; and then run the following
command from the root of the repository:

    python gencopy.py

The script will copy the `libtemplate` repository to the path specified by
`path_to_new_repo_root`, with all library name, author name, copyright year,
email, and library description placeholders replaced by the strings stored in
`new_lib_name_for_imports`, `author_name`, `copyright_year`, `email`, and
`lib_description` respectively.