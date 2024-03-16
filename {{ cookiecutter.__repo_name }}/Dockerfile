# Dockerfile may have following Arguments:
# tag - tag for the Base image, (e.g. 2.9.1 for tensorflow)
#
# To build the image:
# $ docker build -t <dockerhub_user>/<dockerhub_repo> --build-arg arg=value .
# or using default args:
# $ docker build -t <dockerhub_user>/<dockerhub_repo> .
#
# [!] Note: For the Jenkins CI/CD pipeline, input args are defined inside the
# Jenkinsfile, not here!

ARG tag={{ cookiecutter.__baseimage_cpu_tag }}

# Base image, e.g. tensorflow/tensorflow:2.9.1
FROM ai4oshub/{{ cookiecutter.docker_baseimage }}:${tag}

LABEL maintainer='{{ cookiecutter.author_name }}'
LABEL version='{{ cookiecutter.app_version }}'
# {{ cookiecutter.description.replace('\'', '') }}

# Download new model weights and remove old ones
# You can use the following as "reference" - https://github.com/ai4os-hub/ai4os-image-classification-tf/blob/master/Dockerfile
###############
### FILL ME ###
###############
