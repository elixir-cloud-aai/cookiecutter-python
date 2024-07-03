\[!\[Actions status\](https://github.com/elixir-cloud-aai/Python
Cookiecutter/workflows/CI/badge.svg)\](https://github.com/elixir-cloud-aai/Python
Cookiecutter/actions)
[![Bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://bandit.readthedocs.io/en/latest/)
\[!\[codecov\](https://codecov.io/gh/elixir-cloud-aai/Python
Cookiecutter/branch/main/graph/badge.svg)\](https://codecov.io/gh/elixir-cloud-aai/Python
Cookiecutter)
[![Documentation Status](https://readthedocs.org/projects/python_cookiecutter/badge/?version=latest)](https://python_cookiecutter.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-311/)
\[!\[GitHub
contributors\](https://img.shields.io/github/contributors/elixir-cloud-aai/Python
Cookiecutter)\](https://github.com/elixir-cloud-aai/Python
Cookiecutter/graphs/contributors)
[![Ruff](https://img.shields.io/badge/linter%20&%20formatter-ruff-000000.svg)](https://docs.astral.sh/ruff/)
[![Safety](https://img.shields.io/badge/security-safety-orange.svg)](https://safetycli.com/product/safety-cli)

# {{ cookiecutter.project_name }}

{{ cookiecutter.short_description }}

## Table of Contents

- [Basic Usage](#basic-usage)
- [Installation](#installation)
- [Development](#development)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [Versioning](#versioning)
- [License](#license)
- [Contact](#contact)

## Basic Usage

## Installation

## Development

For ease, certain scripts have been abbreviated in `Makefile`, make sure that
have installed the dependencies before running the commands.

> **Note**: `make` commands are only available for Unix-based systems.

To view the commdands available, run:

```sh
make
```

Here are certain commands that you might find useful:

- Making a virtual environment

```sh
make v
```

- Installing dependencies

```sh
make i
```

- Running tests

```sh
make t
```

- Running linter, formatter and spell checker

```sh
make fl
```

- Building the documentation

```sh
make d
```

- Running type checker

```sh
make tc
```

- Running all pre-commit checks

```sh
make pc
```

> **Note**: This is not the complete list of commands, run `make` to find if
> more have been added.

## Contributing

This project is a community effort and lives off _your_ contributions, be it in
the form of bug reports, feature requests, discussions, fixes or any other form
of contribution!

Please refer to the guidelines available at [`CONTRIBUTING.md`][contributing] if
you are interested in contributing.

## Code of Conduct

Please mind the code of conduct described in
[`CODE_OF_CONDUCT.md`][code-of-conduct] for all interactions with the community.
Please be nice to one another! :)

If you experience any unacceptable behavior by any member of the community,
please refer to the contact method specified in
[`CODE_OF_CONDUCT.md`][code-of-conduct] to report the incident to the community
leaders.

## Versioning

The project adopts the [semantic versioning](https://semver.org/) scheme for
versioning. Currently the software is in a pre-release stage, so changes to the
API, including breaking changes, may occur at any time without further notice.

## License

This project is distributed under the [Apache License 2.0][badge-license-url], a
copy of which is also available in [`LICENSE`][license].

## Contact

The project is maintained by [ELIXIR Cloud & AAI][elixir-cloud-aai], a Driver
Project of the [Global Alliance for Genomics and Health (GA4GH)][ga4gh], under
the umbrella of the [ELIXIR][elixir] [Compute Platform][elixir-compute].

To get in touch with us, please use one of the following routes:

- For filing bug reports, feature requests or other code-related issues, please
  make use of the project's \[issue
  tracker\](https://github.com/elixir-cloud-aai/Python Cookiecutter/issues).
- For private/personal issues, more involved communication, or if you would like
  to join our team as a regular contributor, you can either join our
  [chat board][badge-chat-url] or [email] the community leaders.

[![logo-elixir]][elixir] [![logo-elixir-cloud-aai]][elixir-cloud-aai]

[badge-chat-url]: https://join.slack.com/t/elixir-cloud/shared_invite/enQtNzA3NTQ5Mzg2NjQ3LTZjZGI1OGQ5ZTRiOTRkY2ExMGUxNmQyODAxMDdjM2EyZDQ1YWM0ZGFjOTJhNzg5NjE0YmJiZTZhZDVhOWE4MWM
[badge-license-url]: http://www.apache.org/licenses/LICENSE-2.0
[code-of-conduct]: CODE_OF_CONDUCT.md
[contributing]: https://elixir-cloud-aai.github.io/guides/guide-contributor/
[elixir]: https://elixir-europe.org/
[elixir-cloud-aai]: https://elixir-cloud.dcc.sib.swiss/
[elixir-compute]: https://elixir-europe.org/platforms/compute
[email]: mailto:cloud-service@elixir-europe.org
[ga4gh]: https://ga4gh.org/
[license]: LICENSE
[logo-elixir]: images/logo-elixir.svg
[logo-elixir-cloud-aai]: images/logo-elixir-cloud-aai.svg
