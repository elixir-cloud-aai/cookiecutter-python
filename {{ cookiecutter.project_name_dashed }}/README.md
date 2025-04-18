[![Bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://bandit.readthedocs.io/en/latest/)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name_dashed }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name_dashed }})
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)][code-of-conduct]
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_name_dashed }}/badge/?version=latest)](https://{{ cookiecutter.project_name_dashed }}.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)
[![Python {{ cookiecutter.python_version }}](https://img.shields.io/badge/python-{{ cookiecutter.python_version }}-blue.svg)](https://www.python.org/)
[![GitHub contributors](https://img.shields.io/github/contributors/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name_dashed }})](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name_dashed }}/graphs/contributors)
[![Ruff](https://img.shields.io/badge/linter%20&%20formatter-ruff-000000.svg)](https://docs.astral.sh/ruff/)
[![Safety](https://img.shields.io/badge/security-safety-orange.svg)](https://safetycli.com/product/safety-cli)

# {{ cookiecutter.project_name }}

{{ cookiecutter.short_description }}

## Table of Contents

- [Basic Usage](#basic-usage)
- [Installation](#installation)
- [Development](#development)
  - [Makefile](#makefile)
  - [Environment reproducibility](#environment-reproducibility)
    - [asdf](#asdf)
    - [Dev containers](#dev-containers)
    - [Editor config](#editor-config)
    - [Setting environment variables (direnv)](#setting-environment-variables-direnv)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [Versioning](#versioning)
- [License](#license)
- [Contact](#contact)

## Basic Usage

## Installation

## Development

### Makefile

For ease of use, certain scripts have been abbreviated in `Makefile`, make sure
that you have installed the dependencies before running the commands.

> **Note**: `make` commands are only available for Unix-based systems.

To view the commands available, run:

```sh
make
```

Here are certain commands that you might find useful:

- Make a virtual environment

```sh
make v
```

- Install all dependencies including optional dependencies

```sh
make i
```

> **Note**: This project uses optional dependency groups such as `types`,
> `code_quality`, `docs`, `vulnerability`, `test`, and `misc`. To install stubs
> or types for the dependencies, you **must** use the following command:
>
> ```sh
> poetry add types-foo --group types
> ```
>
> Replace `types-foo` with the name of the package for the types. All runtime
> dependencies should be added to the `default` group. For example, to install
> `requests` and its type stubs, run:
>
> ```sh
> poetry add requests
> poetry add types-requests --group types
> ```
>
> This ensures that the type checker functions correctly.
>
> **Note**: Since the dependencies are segregated into groups, if you add a new
> group make sure to add it in `make install` command in [Makefile](Makefile).

- Run tests

```sh
make t
```

- Run linter, formatter and spell checker

```sh
make fl
```

- Build the documentation

```sh
make d
```

> **Note**: If you make changes to the code, make sure to generate and push the
> documentation using above command, else the documentation check CI will fail.
> Do NOT edit auto-generated documentation manually.

- Run type checker

```sh
make tc
```

- Run all pre-commit checks

```sh
make pc
```

- Update the cookiecutter template

```sh
make u
```

> **Note**: This is not the complete list of commands, run `make` to find out if
> more have been added.

### Environment reproducibility

Below mentioned are some tools and configuration that you can use to make your
environment development-ready. This is optional and opinionated but can help you
set up your environment quickly.

#### asdf

We recommend using [asdf][asdf] to manage your development environment
efficiently. This tool allows you to handle multiple language versions and tools
seamlessly. You can install asdf by following the
[official installation guide][asdf-install]. If you are working within
[dev containers](#dev-containers), asdf will come pre-installed.

The project includes a `.tool-versions` file, which lists the specific versions
of tools used. This ensures consistency across environments. To streamline the
installation process, use the following command to install the required tools
defined in the `.tool-versions` file:

```sh
make asdfi
```

> **Note:** The `make asdfi` command might not install every tool listed in
> the `.tool-versions` file. After running the command, verify that all
> necessary tools are installed. If any tools are missing, install them
> manually using asdf.

Example manual installation command:

```sh
asdf install <tool-name> <version>
```

#### Dev Containers

Our project supports [Dev Containers][devcontainers] for an easy and reproducible
setup of development environments via containers. To make use of it, install the
Dev Containers extension in one of the supported editors/IDEs.

For example, for VS Code, do the following to have Dev Containers provision a
container-based development environment for you:

- Make sure [Docker is installed][docker-install] on your machine.
- To install the official Microsoft extension, open the Extensions view
  (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>x</kbd>), enter
  `ms-vscode-remote.remote-containers` in the query box, press <kbd>Enter</kbd>,
  select the "Dev Containers" extension and hit the "Install" button;
  alternatively, use [this direct link][devcontainers-download]
- After reloading VS Code and opening the project folder, you should be prompted
  by the Dev Containers extension to open the workspace in a container. If not,
  press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>g</kbd> to open the command
  panel, search for "Dev Containers: Open Workspace in Container..." and hit
  <kbd>Enter</kbd>

The development environment will now be installed and activated.

> **Note:** The initial process will take some time, as multiple container images
> need to be pulled and dependencies installed. However, once set up, activating
> the environment is fast.

#### Editor Config

To ensure a consistent code style across the project, we include an `.editorconfig`
file that defines the coding styles for different editors and IDEs. Most modern
editors support this file format out of the box, but you might need to install a
plugin for some editors. Please refer to the [EditorConfig website][editor-config].


#### Setting environment variables (direnv)

Our project uses [.envrc files][direnv] to manage environment variables.
Wherever such a file is required across the project tree, you will find a
`.envrc.template` file that contains the necessary variables and helps you
create your own personal copy of each file. You can find the locations of all
`.envrc.template` files by executing `find . -type f -name \.envrc\.template`
in the root directory. For each, create a copy named `.envrc` in the same
directory, open it in a text editor and replace the template/example values with
your own personal and potentially confidential values.

**Warning:** Be careful not to leak sensitive information! In particular,
**never** add your secrets to the `.envrc.template` files directly, as these are
committed to version control and will be visible to anyone with access to the
repository. Always create an `.envrc` copy first (capitalization and punctuation
matter!), as these (along with `.env` files) are ignored from version control.

Once you have filled in all of your personal information, you can have the
`direnv` tool manage setting your environment variables automatically (depending
on the directory you are currently in and the particular `.envrc` file defined
for that directory) by executing the following command:

```sh
direnv allow
```

> **Note**: Make sure you have `direnv` installed on your system. Follow the
> instructions on the [official website][direnv] to install it. If you are using
> [Dev Containers](#dev-containers), your development environment will have
> `direnv` available and ready to use.

## Contributing

This project is a community effort and lives off _your_ contributions, be it in
the form of bug reports, feature requests, discussions, fixes or any other form
of contribution!

Please refer to the guidelines available at [`CONTRIBUTING.md`][contributing] if
you are interested in contributing.

## Code of Conduct

We kindly request all contributors to abide by our
[organization's Code of Conduct][code-of-conduct]. Please also refer to this
document if you want to report an incident with respect to conduct in our
community. Thank you for your cooperation.

## Versioning

The project adopts the [semantic versioning][semver] scheme for versioning.
Currently the software is in a pre-release stage, so changes to the API,
including breaking changes, may occur at any time without further notice.

## License

This project is distributed under the [Apache License 2.0][badge-license-url], a
copy of which is also available in [`LICENSE`][license].

## Contact

The project is maintained by [ELIXIR Cloud & AAI][elixir-cloud-aai], a Driver
Project of the [Global Alliance for Genomics and Health (GA4GH)][ga4gh], under
the umbrella of the [ELIXIR] [Compute Platform][elixir-compute].

To get in touch with us, please use one of the following routes:

- For filing bug reports, feature requests or other code-related issues, please
  make use of the project's [issue tracker][issue-tracker].
- For private/personal issues, more involved communication, or if you would like
  to join our team as a regular contributor, you can either join our
  [chat board][badge-chat-url] or [email] the community leaders.

[![logo-elixir]][elixir] [![logo-elixir-cloud-aai]][elixir-cloud-aai]

[asdf]: https://asdf-vm.com/
[asdf-install]: https://asdf-vm.com/guide/getting-started.html
[badge-chat-url]: https://join.slack.com/t/elixir-cloud/shared_invite/enQtNzA3NTQ5Mzg2NjQ3LTZjZGI1OGQ5ZTRiOTRkY2ExMGUxNmQyODAxMDdjM2EyZDQ1YWM0ZGFjOTJhNzg5NjE0YmJiZTZhZDVhOWE4MWM
[badge-license-url]: http://www.apache.org/licenses/LICENSE-2.0
[code-of-conduct]: https://elixir-cloud-aai.github.io/about/code-of-conduct/
[contributing]: https://elixir-cloud-aai.github.io/guides/guide-contributor/
[devcontainers]: https://code.visualstudio.com/docs/devcontainers/containers
[devcontainers-download]: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
[direnv]: https://direnv.net/
[docker-install]: https://docs.docker.com/engine/install/
[editor-config]: https://editorconfig.org/
[elixir]: https://elixir-europe.org/
[elixir-cloud-aai]: https://elixir-cloud.dcc.sib.swiss/
[elixir-compute]: https://elixir-europe.org/platforms/compute
[email]: mailto:cloud-service@elixir-europe.org
[ga4gh]: https://ga4gh.org/
[issue-tracker]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name_dashed }}/issues
[license]: LICENSE
[logo-elixir]: images/logo-elixir.svg
[logo-elixir-cloud-aai]: images/logo-elixir-cloud-aai.svg
[semver]: https://semver.org/
