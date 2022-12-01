#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 - 2019 Karlsruhe Institute of Technology - Steinbuch Centre for Computing
# This code is distributed under the MIT License
# Please, see the LICENSE file

"""
    Post-hook script
    Moves DEEP-OC-{{ cookiecutter.repo_name }} directory one level up.
    Initialized Git repositories
    Creates 'test' branch
    Switches back to 'master'
"""
import os
import re
import shutil
import subprocess as subp
import sys

REPO_REGEX = r'^[a-z][_a-z0-9]+$'

repo_name = '{{ cookiecutter.repo_name }}'
deep_oc = 'DEEP-OC-{{ cookiecutter.repo_name }}'
deep_oc_dir = os.path.join("../", deep_oc)

if not re.match(REPO_REGEX, repo_name):
    print("")
    print("[ERROR]: %s is not a valid Python package name!" % repo_name)
    print("         Please, use low case and no dashes!")

    # exits with status 1 to indicate failure
    sys.exit(1)


def git_ini(repo):
    """ Function
        Initializes Git repository
    """
    gitrepo = ('{{ cookiecutter.git_base_url }}'.rstrip('/')
                + "/" + repo + '.git')
    try:
        os.chdir("../" + repo)
        subp.call(["git", "init"])
        subp.call(["git", "add", "."])
        subp.call(["git", "commit", "-m", "initial commit"])
        subp.call(["git", "remote", "add", "origin", gitrepo])

        # create test branch automatically
        subp.call(["git", "checkout", "-b", "test"])
        # adjust [Build Status] for the test branch
        readme_content=[]
        with open("README.md") as f_old:
            for line in f_old:
                if "[![Build Status]" in line:
                    line = line.replace("/master)", "/test)")
                readme_content.append(line)

        with open("README.md", "w") as f_new:
            for line in readme_content:
                f_new.write(line)

        subp.call(["git", "commit", "-a", "-m", "update README.md for the BuildStatus"])

        # switch back to master
        subp.call(["git", "checkout", "master"])
    except OSError as os_error:
        sys.stdout.write('[Error] Creating git repository failed for ' + repo + " !")
        sys.stdout.write('[Error] {} '.format(os_error))
        return "Error"
    else:
        return gitrepo


try:

    # initialized both git repositories
    git_deep_oc = git_ini(deep_oc)

    if "Error" not in git_deep_oc:
        print()
        print("[Info] {} was created successfully,".format(deep_oc))
        print("       Don't forget to create corresponding remote repository: {}".format(git_deep_oc))
        print("       then you can do 'git push origin --all'")

    sys.exit(0)
except OSError as os_error:
    sys.stdout.write(
        'While attempting to move and create git \
         repository an error occurred! '
    )
    sys.stdout.write('Error! {} '.format(os_error))
