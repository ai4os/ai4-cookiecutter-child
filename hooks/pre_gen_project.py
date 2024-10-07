#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 - 2023 Karlsruhe Institute of Technology - Scientific Computing Center
# This code is distributed under the MIT License
# Please, see the LICENSE file

"""
    Pre-hook script
    1. Check that {{ cookiecutter.__repo_name }}:
      a. is not too short (has to be more than one character)
      b. has characters valid for python, dash, and/or underscore
"""

import re
import sys
from urllib.parse import urlparse

# init error_messages
error = False
error_messages = []

def check_url(url):
    """Function to check URL"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

git_base_url = "https://github.com/ai4os-hub"


# check {{ cookiecutter.__repo_name }}
MODULE_REGEX = r'^[a-zA-Z][a-zA-Z0-9-_]+$'
repo_name = '{{ cookiecutter.__repo_name }}'
if (not re.match(MODULE_REGEX, repo_name) or
    len(repo_name) < 2):
    message = ("'{}' is not a valid module name! ".format(repo_name) +
               "Use characters, numbers, dashes and/or underscores!" +
               "Please, check the 'project_name' input")
    print("[ERROR]: " + message)
    error = True
    error_messages.append(message)

if error:
    sys.exit("; ".join(error_messages))
