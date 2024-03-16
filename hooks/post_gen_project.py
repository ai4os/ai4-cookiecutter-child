#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 - 2024 Karlsruhe Institute of Technology - Steinbuch Centre for Computing
# This code is distributed under the MIT License
# Please, see the LICENSE file

""" 
    Post-hook script
    Initializes Git repository
    Creates 'test' branch
    Switches back to 'main'
"""
import os
import re
import requests
import shutil
import subprocess as subp
import sys

REPO_REGEX = r'^[a-zA-Z][a-zA-Z0-9-_]+$'

repo_name = '{{ cookiecutter.__repo_name }}'
defaultbranch = 'main'

if not re.match(REPO_REGEX, repo_name):
    message = ("'{}' is not a valid module name! ".format(repo_name) +
               "Please, use characters, numbers, dashes and/or underscores!" +
               "Please, check the 'project_name' input")

    print("[ERROR]: " + message)

    # exits with status 1 to indicate failure
    sys.exit(1)

def update_jenkinsconstants(repo):
    """Function
       Checks for 'gpu' tag and updates JenkinsConstants.groovy
    """
    
    baseimage = '{{ cookiecutter.__docker_baseimage }}'
    baseimage = baseimage.rstrip('/')
    baseimage_tag = '{{ cookiecutter.__baseimage_tag }}'

    url = ("https://hub.docker.com/v2/repositories/ai4oshub/" +
           baseimage + "/tags/gpu/")

    # check if tag "gpu" exists
    r = requests.get(url)
    if r.status_code == 200:
        text=F"""
@Field
def base_cpu_tag = '{baseimage_tag}'

@Field
def base_gpu_tag = 'gpu'

return this;
"""
    else:
        text=F"""
// If <docker_baseimage> has separate CPU and GPU versions
// uncomment following lines and define both values
//@Field
//def base_cpu_tag = '{baseimage_tag}'
//
//@Field
//def base_gpu_tag = 'gpu'

return this;
"""

    with open("../" + repo + "/JenkinsConstants.groovy", "a") as jcfile:
        jcfile.write(text)

def git_ini(repo):
    """ Function
        Initializes Git repository
    """
    gitrepo = ('{{ cookiecutter.git_base_url }}'.rstrip('/')
                + "/" +  repo + '.git')
    try:
        os.chdir("../" + repo)
        subp.call(["git", "init", "-b", defaultbranch])
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
                    line = line.replace("/main)", "/test)")
                readme_content.append(line)

        with open("README.md", "w") as f_new:
            for line in readme_content:
                f_new.write(line)

        subp.call(["git", "commit", "-a", "-m", "update README.md for the BuildStatus"])

        # switch back to main
        subp.call(["git", "checkout", "main"])
    except OSError as os_error:
        sys.stdout.write('[Error] Creating git repository failed for ' + repo + " !")
        sys.stdout.write('[Error] {} '.format(os_error))
        return "Error"
    else:
        return gitrepo

try:
    # update JenkinsConstatns.groovy
    update_jenkinsconstants(repo_name.rstrip('/'))

    # initialize git repository
    git_user_app = git_ini(repo_name)

    if "Error" not in git_user_app:
        print()
        print("[Info] {} was created successfully,".format(repo_name))
        print("       Don't forget to create corresponding remote repository: {}".format(git_user_app))
        print("       then you can do 'git push origin --all'")
        print()

    sys.exit(0)
except OSError as os_error:
    sys.stdout.write(
        'While attempting to create git repository an error occurred! '
    )
    sys.stdout.write('Error! {} '.format(os_error))
