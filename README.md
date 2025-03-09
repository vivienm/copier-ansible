# Ansible project template

An opinionated [Copier](https://copier.readthedocs.io/en/stable/) template for Ansible playbooks.

## Quickstart

To install Copier, please follow the installation instructions [here](https://copier.readthedocs.io/en/stable/#installation).

Then, to create a new project based on this template, run:

```shell
copier copy 'https://github.com/vivienm/copier-ansible' path/to/your/project
```

and fill in the form.

Go to the project directory, create the password file (only for playbooks) and run the tests:

```shell
vault/password.py --init
just ci
```

The project is ready!

To update an existing project based on this template, run:

```shell
copier update --skip-answered
```
