import groovy.transform.Field
// This file defines variables to be used in the AI4OS-Hub Upstream Jenkins pipeline
// dockerfile : what Dockerfile to use for building, can include path, e.g. docker/Dockerfile
// If *both*, CPU and GPU versions can be built:
// base_cpu_tag : CPU tag for the base docker image (check your Dockerfile)
// base_gpu_tag : GPU tag for the base docker image (check your Dockerfile)

@Field
def dockerfile = 'Dockerfile'

{% if (curl --silent -f --head -1L https://hub.docker.com/v2/repositories/ai4oshub/cookiecutter.docker_baseimage/tags/gpu/ > /dev/null)  %}
@Field
def base_cpu_tag = '{{ cookiecutter.__baseimage_tag }}'

@Field
def base_gpu_tag = 'gpu'

{% else %}
// If <docker_baseimage> has separate CPU and GPU versions
// uncomment following lines and define both values
//@Field
//def base_cpu_tag = '{{ cookiecutter.__baseimage_tag }}'
//
//@Field
//def base_gpu_tag = '{{ cookiecutter.__baseimage_gpu_tag }}'
{% endif %}

return this;