# Ansible project template

An opinionated [Copier](https://copier.readthedocs.io/en/stable/) template for [Ansible](https://docs.ansible.com/) projects.

## Features

* Dependency management with [uv](https://docs.astral.sh/uv/).
* Vault management with [GPG](https://gnupg.org/).
* Linting with [Ansible Lint](https://ansible-lint.readthedocs.io/en/latest/).
* Task automation with [just](https://github.com/casey/just).
* CI with [GitHub actions](https://github.com/features/actions).

## Quickstart

To install Copier, please follow the installation instructions [here](https://copier.readthedocs.io/en/stable/#installation).

Then, to create a new project based on this template, run:

```bash
copier copy 'https://github.com/vivienm/copier-ansible' path/to/your/project
```

and fill in the form.

Go to the project directory, create the password file (only for playbooks) and run the tests:

```bash
vault/password.py --init
just ci
```

The project is ready!

To update an existing project based on this template, run:

```bash
copier update --skip-answered
```
