"""Generate a copy of template with updated library and author information.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For directory operations, e.g. to check if a directory exists.
import os

# For pattern matching.
import re

# For enforcing character limits for lines of texts.
import textwrap

# For copying directories.
import shutil



############################
## Authorship information ##
############################

__author__     = "Matthew Fitzpatrick"
__copyright__  = "Copyright 2023"
__credits__    = ["Matthew Fitzpatrick"]
__maintainer__ = "Matthew Fitzpatrick"
__email__      = "mrfitzpa@uvic.ca"
__status__     = "Development"



###########################
## Define body of script ##
###########################

# The library name as it would appear for imports: ``import some_lib_name``.
new_lib_name_for_imports = "libname"

# An unabbreviated alternative library name to appear in the documentation.
new_lib_name_for_docs = "New Library Name"

# Authorship information.
author_name = "John Smith"
copyright_year = "2023"
email = "jsmith@domain.com"

# Short description of library, ideally one line.
lib_description = ("Insert short description of library here.")

# Path to new repository. If ``path_to_new_repo_root`` is set to ``None``, then
# the new repository is created at the path
# ``<old-repo-root>/../<new-lib-name-for-imports>``, where ``<old-repo-root>``
# is the path to the old/template repository, and ``<new-lib-name-for-imports>``
# is the new library name, as it would appear for imports, i.e. the name
# specified by the variable ``new_lib_name_for_imports`` above.
path_to_new_repo_root = None

# The target git platform on which to save a remote copy of your local
# repository, should you decide to do so. Currently supported options are
# ``"github"`` and ``"gitlab"``. The code below will then generate the files
# required to enable the hosting of the library's documentation in web form on
# said git platform. Users can still save remote copies on different git
# platforms, e.g. bitbucket, however there is no guarantee that the library's
# documentation can be viewed in web form.  In this latter case, users are
# probably better off setting the variable ``target_git_platform`` to
# ``"github"``.
target_git_platform = "github"



# The remainder of the script should not be modified.



def _generate_default_path_to_old_repo_root():
    path_to_current_script = os.path.realpath(__file__)
    path_to_old_repo_root = os.path.dirname(path_to_current_script)

    return path_to_old_repo_root



def _generate_default_path_to_new_repo_root():
    path_to_old_repo_root = _generate_default_path_to_old_repo_root()
    up_one_level_dirname = os.path.dirname(path_to_old_repo_root)
    path_to_new_repo_root = (up_one_level_dirname
                             + "/" + new_lib_name_for_imports)

    return path_to_new_repo_root



_path_to_old_repo_root = _generate_default_path_to_old_repo_root()
if path_to_new_repo_root is None:
    path_to_new_repo_root = _generate_default_path_to_new_repo_root()



def _str_is_left_aligned_header_or_paragraph_text(string):
    string = string.rstrip()

    if (len(string) > 0) and (not (re.fullmatch("=+", string)
                                   or re.fullmatch("-+", string)
                                   or re.match("\.\. _[a-zA-Z]+", string)
                                   or re.match("\.\. \[", string)
                                   or re.match(" +", string)
                                   or re.match("\t", string)
                                   or re.match("[\*\+\-] ", string))):
        result = True
    else:
        result = False

    return result



_str_replacement_map = {"libtemplate": new_lib_name_for_imports,
                        "author-placeholder": author_name,
                        "copyright-year-placeholder": copyright_year,
                        "email-placeholder": email,
                        "library-description-placeholder": lib_description}



def _apply_str_replacements_to_lines(lines):
    for line_idx, line in enumerate(lines):
        line = line.rstrip()
        for old_substring, new_substring in _str_replacement_map.items():
            line = line.replace(old_substring, new_substring)
        lines[line_idx] = line
        if re.fullmatch("=+", line) or re.fullmatch("-+", line):
            lines[line_idx] = line[0]*len(lines[line_idx-1])

    return lines



def _generate_new_file_contents(filename):
    with open(filename, "r") as file_obj:
        lines = file_obj.read().splitlines()

    lines = _apply_str_replacements_to_lines(lines)

    return lines



def _generate_new_rst_file_contents(filename):
    with open(filename, "r") as file_obj:
        lines = file_obj.read().splitlines()

    lines = _apply_str_replacements_to_lines(lines)

    end_of_file_not_reached = True
    line_idx = 0
    while end_of_file_not_reached:
        line_1 = lines[line_idx].rstrip()

        if _str_is_left_aligned_header_or_paragraph_text(line_1):
            end_of_paragraph_not_reached = True
            while end_of_paragraph_not_reached:
                if line_idx+1 < len(lines):
                    line_2 = lines[line_idx+1].rstrip()
                    if _str_is_left_aligned_header_or_paragraph_text(line_2):
                        line_1 += " " + line_2
                        lines.pop(line_idx+1)
                    else:
                        end_of_paragraph_not_reached = False
                else:
                    end_of_paragraph_not_reached = False

            replacement_lines = textwrap.wrap(line_1,
                                              width=80,
                                              break_long_words=False)
        else:
            replacement_lines = [line_1]

        lines = lines[:line_idx] + replacement_lines + lines[line_idx+1:]

        line_idx += len(replacement_lines)
        if line_idx >= len(lines):
            end_of_file_not_reached = False

    return lines



def _generate_new_root_README_md_file_contents():
    lines = ("# "+new_lib_name_for_docs+" ("+new_lib_name_for_imports+")",
             "",
             "Insert here a brief description of the library and any other "
             "information that",
             "would be helpful to new users.")

    return lines



def _generate_new_root_docs_license_rst_file_contents():
    lines = ("License",
             "=======",
             "",
             "The source code documented here is published under a [INSERT "
             "LICENSE TYPE]",
             "license, which we include below.",
             "",
             ".. include:: ../LICENSE",
             "    :literal:")

    return lines



def _generate_new_root_docs_index_rst_file_contents():
    lines = [new_lib_name_for_docs+" ("+new_lib_name_for_imports+")",
             "="*(len(new_lib_name_for_docs)+len(new_lib_name_for_imports)+3),
             "",
             "Insert here a brief description of the library and any other "
             "information that",
             "would be helpful to new users.",
             ""]
    
    with open(path_to_new_repo_root + "/docs/index.rst", "r") as file_obj:
        lines += file_obj.read().splitlines()[-21:]
        
    for line_idx, line in enumerate(lines):
        lines[line_idx] = line.replace("libtemplate", new_lib_name_for_imports)

    return lines



def _wrap_single_line_python_comment(line):
    line = line.rstrip()
    indent = len(line) - len(line.lstrip())
    line = line.lstrip()[2:]

    width = 80 - indent - 2

    replacement_lines = textwrap.wrap(line, width=width, break_long_words=False)
    for line_idx, replacement_line in enumerate(replacement_lines):
        replacement_lines[line_idx] = (" "*indent) + "# " + replacement_line

    return replacement_lines



def _wrap_single_line_python_doc_string(line):
    line = line.rstrip()
    indent = len(line) - len(line.lstrip())
    line = line.lstrip()

    width = 80 - indent

    replacement_lines = textwrap.wrap(line, width=width, break_long_words=False)
    for line_idx, replacement_line in enumerate(replacement_lines):
        replacement_lines[line_idx] = (" "*indent) + replacement_line

    return replacement_lines



def _generate_new_root_docs_conf_py_file_contents():
    filename = path_to_new_repo_root + "/docs/conf.py"
    with open(filename, "r") as file_obj:
        lines = file_obj.read().splitlines()

    lines = _apply_str_replacements_to_lines(lines)

    line_idx = 26
    replacement_lines = _wrap_single_line_python_comment(lines[line_idx])
    lines = lines[:line_idx] + replacement_lines + lines[line_idx+1:]

    return lines



def _generate_new_root_setup_py_file_contents():
    filename = path_to_new_repo_root + "/setup.py"
    with open(filename, "r") as file_obj:
        lines = file_obj.read().splitlines()

    lines = _apply_str_replacements_to_lines(lines)

    end_of_file_not_reached = True
    line_idx_1 = 0
    while end_of_file_not_reached:
        line = lines[line_idx_1].rstrip()
        if "``{}``".format(new_lib_name_for_imports) in line:
            replacement_lines = _wrap_single_line_python_doc_string(line)
        elif "description =" in line:
            width = 58
            replacement_lines = textwrap.wrap(lib_description,
                                              width=width,
                                              break_long_words=False)
            num_replacement_lines = len(replacement_lines)
            replacement_lines[0] = ("    description = (\""
                                    + replacement_lines[0]
                                    + "\"")
            for line_idx_2 in range(1, num_replacement_lines):
                replacement_lines[line_idx_2] = ("                   \""
                                                 + replacement_lines[line_idx_2]
                                                 + "\"")
            replacement_lines[-1] += ")"
        else:
            replacement_lines = [line]

        lines = lines[:line_idx_1] + replacement_lines + lines[line_idx_1+1:]

        line_idx_1 += len(replacement_lines)
        if line_idx_1 >= len(lines):
            end_of_file_not_reached = False

    return lines



def _generate_new_root_lib_init_py_file_contents():
    filename = (path_to_new_repo_root
                + "/" + new_lib_name_for_imports
                + "/__init__.py")

    lines = ['"""Insert here a brief description of the library.',
             '',
             '"""']
    with open(filename, "r") as file_obj:
        lines += file_obj.read().splitlines()[6:]

    lines = _apply_str_replacements_to_lines(lines)
    for line_idx, line in enumerate(lines):
        if "uses." in line:
            lines.pop(line_idx)

    end_of_file_not_reached = True
    line_idx = 0
    while end_of_file_not_reached:
        line = lines[line_idx].rstrip()
        if "Print information" in line:
            line += " uses."
            replacement_lines = _wrap_single_line_python_doc_string(line)
        else:
            replacement_lines = [line]

        lines = lines[:line_idx] + replacement_lines + lines[line_idx+1:]

        line_idx += len(replacement_lines)
        if line_idx >= len(lines):
            end_of_file_not_reached = False

    return lines



def _generate_new_root_lib_version_py_file_contents():
    filename = (path_to_new_repo_root
                + "/" + new_lib_name_for_imports
                + "/version.py")

    with open(filename, "r") as file_obj:
        lines = file_obj.read().splitlines()

    lines = _apply_str_replacements_to_lines(lines)

    end_of_file_not_reached = True
    line_idx = 0
    while end_of_file_not_reached:
        line = lines[line_idx].rstrip()
        if "# Check versions of" in line:
            replacement_lines = _wrap_single_line_python_comment(line)
        elif "``{}``".format(new_lib_name_for_imports) in line:
            replacement_lines = _wrap_single_line_python_doc_string(line)
        else:
            replacement_lines = [line]

        lines = lines[:line_idx] + replacement_lines + lines[line_idx+1:]

        line_idx += len(replacement_lines)
        if line_idx >= len(lines):
            end_of_file_not_reached = False

    return lines



def _generate_new_root_gitlab_ci_yml_file_contents():
    lines = ["pages:",
             "  stage: deploy",
             "  script:",
             "    - mv docs/_build/html/ public/",
             "  artifacts:",
             "    paths:",
             "    - public",
             "  only:",
             "  - main"]

    return lines



try:
    # Copy select files from the old repository to the new repository.
    ignore = shutil.ignore_patterns(".git",
                                    "gencopy.py",
                                    "gencopy_template.py",
                                    "__pycache__",
                                    "_build",
                                    "_autosummary",
                                    "*~",
                                    "*.pyc",
                                    "reference")
    shutil.copytree(_path_to_old_repo_root,
                    path_to_new_repo_root,
                    ignore=ignore)


    
    # Rename subdirectories in accordance with the new library name.
    os.rename(path_to_new_repo_root + "/libtemplate",
              path_to_new_repo_root + "/" + new_lib_name_for_imports)


    
    # Get directory tree of new library.
    dir_tree = list(os.walk(path_to_new_repo_root))
    if dir_tree == []:
        raise NotADirectoryError("Directory does not exist.")

    dirname = os.path.abspath(dir_tree[0][0])
    basename = os.path.basename(dirname)

    filenames = []
    subdirnames = []

    for x in dir_tree:
        subdirname = x[0]
        subdirnames += [subdirname]

        file_basenames = x[2]
        for file_basename in file_basenames:
            filename = subdirname + '/' + file_basename

            if "~" not in filename and "#" not in filename:
                filenames += [filename]

        subdirnames.pop(0)



    # Insert placeholder values and wrap text if necessary.
    for filename in filenames:
        dirname = os.path.basename(os.path.dirname(filename))
        basename = os.path.basename(filename)
        file_extension = os.path.splitext(filename)[1]
        
        if file_extension == ".rst":
            if basename == "license.rst":
                lines = _generate_new_root_docs_license_rst_file_contents()
            elif basename == "index.rst":
                lines = _generate_new_root_docs_index_rst_file_contents()
            else:
                lines = _generate_new_rst_file_contents(filename)
        elif file_extension == ".py":
            if basename == "conf.py":
                lines = _generate_new_root_docs_conf_py_file_contents()
            elif basename == "setup.py":
                lines = _generate_new_root_setup_py_file_contents()
            elif ((basename == "__init__.py")
                  and (dirname == new_lib_name_for_imports)):
                lines = _generate_new_root_lib_init_py_file_contents()
            elif basename == "version.py":
                lines = _generate_new_root_lib_version_py_file_contents()
            else:
                lines = _generate_new_file_contents(filename)
        elif basename == "README.md":
            lines = _generate_new_root_README_md_file_contents()
        elif basename == "LICENSE":
            lines = ["Insert license here."]
        else:
            lines = _generate_new_file_contents(filename)
                    
        with open(filename, "w") as file_obj:
            new_file_content = "\n".join(lines)
            file_obj.write(new_file_content)



    # Add and remove the files necessary to enable the hosting of the library's
    # documentation in web form on the target git platform.
    if target_git_platform == "gitlab":
        os.remove(path_to_new_repo_root + "/docs/.nojekyll")
        os.remove(path_to_new_repo_root + "/docs/index.html")
        
        lines = _generate_new_root_gitlab_ci_yml_file_contents()
        with open(path_to_new_repo_root + "/.gitlab-ci.yml", "w") as file_obj:
            new_file_content = "\n".join(lines)
            file_obj.write(new_file_content)
        
    
except FileExistsError:
    pass
