#!/usr/bin/env python
"""Generate a copy of template with updated library and author information.
"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For directory operations, e.g. to check if a directory exists.
import os

# For copying directories.
import shutil



############################
## Authorship information ##
############################

__author__     = "Matthew Fitzpatrick"
__copyright__  = "Copyright 2020"
__credits__    = ["Matthew Fitzpatrick"]
__maintainer__ = "Matthew Fitzpatrick"
__email__      = "mrfitzpa@sfu.ca"
__status__     = "Development"



###########################
## Define body of script ##
###########################

# Authorship information.
new_lib_name = "ostfic"
author_name = "Matthew Fitzpatrick"
copyright_year = "2020"
email = "mfitzpatrick@dwavesys.com"

# One-line description of library.
lib_description = "For simulating open-system dynamics of quantum Ising chains."



# Copy library template to new directory.
path_to_current_script = os.path.realpath(__file__)
dirname_of_current_script = os.path.dirname(path_to_current_script)
up_one_level_dirname = os.path.dirname(dirname_of_current_script)
dirname_of_new_repo = up_one_level_dirname + "/" + new_lib_name

try:
    shutil.copytree(dirname_of_current_script,
                    dirname_of_new_repo,
                    ignore = shutil.ignore_patterns(".git",
                                                    "gencopy.py",
                                                    "__pycache__",
                                                    "_build",
                                                    "*~",
                                                    "*.pyc",
                                                    "docs/reference"))

    os.rename(dirname_of_new_repo + "/libtemplate",
              dirname_of_new_repo + "/" + new_lib_name)

    # Get directory tree of new library.
    dir_tree = list(os.walk(dirname_of_new_repo))
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
                    and (new_lib_name + "/" + new_lib_name not in filename)):
                    line = line.replace("libtemplate",
                                        new_lib_name)
                if "docs/license.rst" in filename:
                    if i == 0:
                        lines[0] = line
                    if i == 1:
                        lines[1] = "=" * (len(new_lib_name) + 15) + "\n"
                    elif i == 9:
                        lines[9] = ("The source code documented here is "
                                    "published under a [INSERT LICENSE TYPE]"
                                    "\n")
                    elif i == 10:
                        lines[10] = ("license, which we include below.\n")
                elif ("docs/reference.rst" in filename) and (i == 1):
                    lines[1] = "=" * (len(new_lib_name) + 10) + "\n"
                else:
                    lines[i] = line
            
        with open(filename, "w") as f:
            if new_lib_name + "/LICENSE" in filename:
                new_file_content = "Insert license here."
            else:
                new_file_content = ""
                for line in lines:
                    new_file_content += line
            f.write(new_file_content)
    
except FileExistsError:
    pass
