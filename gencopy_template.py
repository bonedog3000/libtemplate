"""Generate a copy of template with updated library and author information.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For directory operations, e.g. to check if a directory exists.
import os

# For copying directories.
import shutil

# For enforcing 80 character-per-line limits in text files.
import textwrap



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
new_lib_name_for_imports = "some_lib_name"

# An unabbreviated alternative library name to appear in the documentation.
new_lib_name_for_docs = "Some Library Name"

# Authorship information.
author_name = "John Smith"
copyright_year = "2023"
email = "jsmith@domain.com"

# Short description of library, ideally one line.
lib_description = "Insert short description of library here."



# Copy library template to new directory.
path_to_current_script = os.path.realpath(__file__)
path_to_old_repo_root = os.path.dirname(path_to_current_script)
up_one_level_dirname = os.path.dirname(path_to_old_repo_root)
path_to_new_repo_root = up_one_level_dirname + "/" + new_lib_name_for_imports



def generate_new_root_README_md_file_contents():
    lines = ("# "+new_lib_name_for_docs+" ("+new_lib_name_for_imports+")",
             "",
             "Insert here a brief description of the library and any other "
             "information that",
             "would be helpful to new users.")

    return lines



def generate_new_root_CHANGELOG_rst_file_contents():
    filename = path_to_old_repo_root + "/CHANGELOG.rst"
    with open(filename, "r") as file_obj:
        lines = file_obj.read().splitlines()

    for line_idx, line in enumerate(lines):
        lines[line_idx] = line.replace("libtemplate", new_lib_name_for_imports)
        
    line = lines.pop(3) + " " + lines.pop(3)
    line = textwrap.fill(line, width=80)
    lines = lines[:3] + line.split("\n") + lines[3:]

    lines = tuple(lines)

    return lines



def generate_new_root_docs_license_rst_file_contents():
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



def generate_new_root_docs_index_rst_file_contents():
    lines = [new_lib_name_for_docs+" ("+new_lib_name_for_imports+")",
             "="*(len(new_lib_name_for_docs)+len(new_lib_name_for_imports)+3),
             "",
             "Insert here a brief description of the library and any other "
             "information that",
             "would be helpful to new users.",
             ""]
    
    with open(path_to_old_repo_root + "/docs/index.rst", "r") as file_obj:
        lines += file_obj.read().splitlines()[-21:]
        
    for line_idx, line in enumerate(lines):
        lines[line_idx] = line.replace("libtemplate", new_lib_name_for_imports)

    lines = tuple(lines)

    return lines



def generate_new_root_docs_api_rst_file_contents():
    filename = path_to_old_repo_root + "/docs/api.rst"
    with open(filename, "r") as file_obj:
        lines = file_obj.read().splitlines()

    for line_idx, line in enumerate(lines):
        lines[line_idx] = line.replace("libtemplate", new_lib_name_for_imports)
        
    lines[3] = "="*len(lines[2])

    lines = tuple(lines)

    return lines



def generate_new_root_docs_INSTALL_rst_file_contents():
    filename = path_to_old_repo_root + "/docs/INSTALL.rst"
    with open(filename, "r") as file_obj:
        lines = file_obj.read().splitlines()

    for line_idx, line in enumerate(lines):
        lines[line_idx] = line.replace("libtemplate", new_lib_name_for_imports)

    line_indices = (6, 38, 52, 61)
    for line_idx in line_indices:
        lines[line_idx] = "-"*len(lines[line_idx-1])

    lines = tuple(lines)

    return lines



def generate_new_root_docs_literature_rst_file_contents():
    filename = path_to_old_repo_root + "/docs/literature.rst"
    with open(filename, "r") as file_obj:
        lines = file_obj.read().splitlines()

    for line_idx, line in enumerate(lines):
        lines[line_idx] = line.replace("libtemplate", new_lib_name_for_imports)
        
    line = lines.pop(3) + " " + lines.pop(3)
    line = textwrap.fill(line, width=80)
    lines = lines[:3] + line.split("\n") + lines[3:]

    lines = tuple(lines)

    return lines



def generate_new_root_docs_examples_rst_file_contents():
    filename = path_to_old_repo_root + "/docs/examples.rst"
    with open(filename, "r") as file_obj:
        lines = file_obj.read().splitlines()

    for line_idx, line in enumerate(lines):
        lines[line_idx] = line.replace("libtemplate", new_lib_name_for_imports)
        
    line = (lines.pop(5) + " " + lines.pop(5)
            + " " + lines.pop(5) + " " + lines.pop(5))
    line = textwrap.fill(line, width=80)
    lines = lines[:5] + line.split("\n") + lines[5:]

    lines = tuple(lines)

    return lines



try:
    shutil.copytree(path_to_old_repo_root,
                    path_to_new_repo_root,
                    ignore = shutil.ignore_patterns(".git",
                                                    "gencopy.py",
                                                    "gencopy_template.py",
                                                    "__pycache__",
                                                    "_build",
                                                    "*~",
                                                    "*.pyc",
                                                    "reference"))

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



    # Insert placeholder values.
    for filename in filenames:
        with open(filename, "r") as f:
            lines = f.readlines()
            num_lines = len(lines)

            for i in range(num_lines):
                line = lines[i]
                num_char_in_line = len(line)
            
                line = line.replace("author-placeholder",
                                    author_name)
                line = line.replace("copyright-year-placeholder",
                                    copyright_year)
                line = line.replace("email-placeholder",
                                    email)
                line = line.replace("library-description-placeholder",
                                    lib_description)

                if (("README.rst" not in filename)
                    and ("INSTALL.rst" not in filename)
                    and (new_lib_name_for_imports + "/" + new_lib_name_for_imports not in filename)):
                    line = line.replace("libtemplate",
                                        new_lib_name_for_imports)
                if "docs/license.rst" in filename:
                    if i == 0:
                        lines[0] = line
                    if i == 1:
                        lines[1] = "=" * (len(new_lib_name_for_imports) + 15) + "\n"
                    elif i == 9:
                        lines[9] = ("The source code documented here is "
                                    "published under a [INSERT LICENSE TYPE]"
                                    "\n")
                    elif i == 10:
                        lines[10] = ("license, which we include below.\n")
                elif ("docs/reference.rst" in filename) and (i == 1):
                    lines[1] = "=" * (len(new_lib_name_for_imports) + 10) + "\n"
                else:
                    lines[i] = line
            
        with open(filename, "w") as f:
            if new_lib_name_for_imports + "/LICENSE" in filename:
                new_file_content = "Insert license here."
            else:
                new_file_content = ""
                for line in lines:
                    new_file_content += line
            f.write(new_file_content)
    
except FileExistsError:
    pass
