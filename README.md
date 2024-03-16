<div align="center">
  <img src="https://ai4eosc.eu/wp-content/uploads/sites/10/2022/09/horizontal-transparent.png" alt="logo" width="500"/>
</div>

# AI4OS Hub Modules Template (child-module)

## For users

This is template specifically tailored to users performing a retraining of an existing at AI4OS-Hub module. It only creates a Docker repo whose container is based on an existing module's Docker image. It uses [Cookiecutter](https://cookiecutter.readthedocs.io) to generate the templates.

There are other versions of the template:
* [main](https://github.com/ai4os/ai4-template): this is a minimal version of the AI4OS Hub template: Simple template, with the minimum requirements to integrate your AI model in AI4OS Hub.

* [advanced](https://github.com/ai4os/ai4-template-adv): this is a more advanced template. It makes more assumptions on how to structure projects and adds more files. If you want to integrate an already existing AI code, which you still want to keep in a separate repository, this template is for you.

To create a new template of your project, either

* install cookiecutter and run it with this template: 
``` bash
pip install cookiecutter
cookiecutter https://github.com/ai4os/ai4-template-child.git
```
* OR visit our Templates Hub service: https://templates.cloud.ai4eosc.eu/ and select the template

Once you answer all the questions, your repository `<your_project>` will be created.

This is what the folder structures look like:

```
<your_project>
######################
├─ Dockerfile             <- Describes main steps on integration of DEEPaaS API and
│                            <your_project> application in one Docker image
│
├─ Jenkinsfile            <- Describes basic Jenkins CI/CD pipeline
│
├─ LICENSE                <- License file
│
├─ README.md              <- README for developers and users.
│
└─ metadata.json          <- Defines information propagated to the DEEP Marketplace
```

More extended documentation can be found [here](http://docs.ai4os.eu/en/latest/user/overview/cookiecutter-template.html).

## For developers

Once you update the template, please, update this `README.md`, and **especially** `cookiecutter.json` file and `"__ai4_template"` entry with the corresponging, incremented version. The convention for the `"__ai4_template"` entry is to provide the template repository name, slash '/' closest version of the template, following [SymVer](https://semver.org/) specs, e.g.

```
"__ai4_template": "ai4-template/2.1.0"
```
OR
```
"__ai4_template": "ai4-template-adv/2.1.0"
```
OR
```
"__ai4_template": "ai4-template-child/2.1.0"