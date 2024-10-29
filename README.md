[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)][code-of-conduct]
[![GitHub contributors](https://img.shields.io/github/contributors/elixir-cloud-aai/cookiecutter-python)](https://github.com/elixir-cloud-aai/cookiecutter-python/graphs/contributors)

# Python Cookiecutter Template

This is a Cookiecutter template for creating a Python project with Poetry,
including configurations for various project settings.

## Table of Contents

- [Usage](#usage)
- [Configurations](#configurations)
  - [Package manager - Poetry](#package-manager---poetry)
  - [Linters and formatters - Ruff](#linters-and-formatters---ruff)
  - [Spell checker - Typos](#spell-checker---typos)
  - [Static type checker - Mypy](#static-type-checker---mypy)
  - [Documentation - Sphinx](#documentation---sphinx)
  - [Testing - pytest and pytest-cov](#testing---pytest-and-pytest-cov)
- [CI/CD - GitHub Actions](#cicd---github-actions)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [Versioning](#versioning)
- [License](#license)
- [Contact](#contact)

## Usage

1.**Install Cruft** (if you haven't already):

```sh
pip install cruft
```

2.**Generate a new project**:

```sh
cruft create https://github.com/elixir-cloud-aai/cookiecutter-python.git
```

3.**Commit and push the generated files** (as applicable to your Git workflow)

Inside the generated project directory:

```sh
git add .
git branch -m main
git commit -m "chore(init): initialize project with https:github.com/elixir-cloud-aai/cookiecutter-python.git"
```

Push the code to the remote repository:

```sh
git remote add origin <your-repo-url>
git push -u origin main
```

> **Note**: If you want to push your code to GitHub and make use of the
> generated GitHub Actions workflows, we recommend you to set up the
> [necessary secrets](#cicd---github-actions) before pushing the code.
> Otherwise some of workflows may fail.

### Don't wanna use Cruft?

You can also use the `cookiecutter` command directly:

1.**Install cookiecutter** (if you haven't already):

```sh
pip install cookiecutter
```

2.**Generate a new project**:

```sh
cookiecutter gh:elixir-cloud-aai/cookiecutter-python
```

> **Note**: If you're using just `cookiecutter`, manually remove
> `update-template` job from `update.yaml` github action workflow file as
> `cookiecutter` doesn't support autosync like Cruft.

## Configurations

### Package manager - Poetry

This project uses [Poetry][poetry-org] as a package manager. Check out the
commands at the [official documentation][poetry-docs].

### Linters and formatters - Ruff

To lint and format `Python` code files, it uses [Ruff][ruff], the default
configuration is set in the `pyproject.toml` file.

```toml
select = [
  "B", # flake8-bugbear
  "E", # pycodestyle
  "F", # Pyflakes
  "I", # isort
  "PL", # pylint
  "SIM", # flake8-simplify
  "UP", # pyupgrade
]
```

To configure it to your needs, refer to the [rules documentation][ruff-linter]
, and for formatter configuration, refer to the [configuration
documentation][ruff-formatter].

### Spell checker - Typos

If you want to ignore certain words, add them to the `pyproject.toml` file,
under the `tool.typos.default.extend-words` key.

```toml
[tool.typos.default.extend-words]
mke = 'mke'
```

For further configuration, refer to the [typos docs][typos-docs].

### Static type checker - Mypy

Change the configuration in `pyproject.toml` file, for further information refer
to the [documentation][mypy-config].

### Documentation - Sphinx

Configuration for Sphinx is in the `docs/source/conf.py` file, for further info
refer to the [Sphinx documentation][sphinx-docs]. The default configuration uses
[furo theme][furo] and [ReadTheDocs][rtd] to host the documentation, you can
change the configuration using `/docs/source/conf.py` and `.readthedocs.yml`
file.

> **Note**: Make sure to set up the `ReadTheDocs` account and add the projects
> to the account to host the documentation.

### Testing - pytest and pytest-cov

Generate a coverage report using `pytest-cov` and uploads it to codecov.io.

> **Note**: Make sure to set up the `Codecov` account and add the project to 
> the account to host the coverage report and add github
> [token](#cicd---github-actions).

## CI/CD - GitHub Actions

Here are the GitHub Actions Secrets that need to be included in the repository
settings:

- `PYPI_TOKEN`: PyPI account password.

    > **Note**: PyPI account token scoped to this repository (requires the
    > project to exist prior to using the Cookiecutter) or to all repositories.
    > To set up the token, visit <https://pypi.org>, log in, go to
    > `Account settings` in the user menu and hit the `Add API token` button in
    > the `API tokens` section. Add a name, choose the scope and create the
    > token.

- `CODECOV_TOKEN`: Codecov token.

    > **Note**: To set up the token, visit <https://codecov.io/>, log in, find the
    > repository that you want to set up (you may need to "Resync") and hit the
    > "Configure" button. The token should show up in the "Coverage" tab.

- `GITHUB_TOKEN`: This token is auto-generated by GitHub Actions for each job,
    so please do NOT set it manually.

    > **Note**: The token needs to be granted the authority to create pull
    > requests. See [GitHub][gh-update-token] for details on how to set this permission.

## Disclaimer

Some of the links and images have been hardcoded with `ELIXIR Cloud & AAI`'s
assets in the documentation, please update them manually if needed. These assets
**MUST** be included for projects owned by ELIXIR Cloud & AAI, but **MUST NOT**
be included for projects that are not (personal projects, projects owned by
other orgs).

**Only `markdown` files and `images/` directory need to be changed.**

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
Currently the service is in a pre-release stage, so changes to the API,
including breaking changes, may occur at any time without further notice.

## License

This project is distributed under the [Apache License 2.0][badge-license-url], a
copy of which is also available in [`LICENSE`][license].

## Contact

The project is maintained by [ELIXIR Cloud & AAI][elixir-cloud-aai], a Driver
Project of the [Global Alliance for Genomics and Health (GA4GH)][ga4gh], under
the umbrella of the [ELIXIR][elixir] [Compute Platform][elixir-compute].

To get in touch with us, please use one of the following routes:

- For filing bug reports, feature requests or other code-related issues,
    please make use of the project's
    [issue tracker](https://github.com/elixir-cloud-aai/cookiecutter-python/issues).
- For private/personal issues, more involved communication, or if you would
    like to join our team as a regular contributor, you can either join our
    [chat board][badge-chat-url] or [email] the community leaders.

[![logo-elixir]][elixir] [![logo-elixir-cloud-aai]][elixir-cloud-aai]

[badge-chat-url]: https://join.slack.com/t/elixir-cloud/shared_invite/enQtNzA3NTQ5Mzg2NjQ3LTZjZGI1OGQ5ZTRiOTRkY2ExMGUxNmQyODAxMDdjM2EyZDQ1YWM0ZGFjOTJhNzg5NjE0YmJiZTZhZDVhOWE4MWM
[badge-license-url]: http://www.apache.org/licenses/LICENSE-2.0
[code-of-conduct]: https://elixir-cloud-aai.github.io/about/code-of-conduct/
[contributing]: https://elixir-cloud-aai.github.io/guides/guide-contributor/
[elixir]: https://elixir-europe.org/
[elixir-cloud-aai]: https://elixir-cloud.dcc.sib.swiss/
[elixir-compute]: https://elixir-europe.org/platforms/compute
[email]: mailto:cloud-service@elixir-europe.org
[ga4gh]: https://ga4gh.org/
[gh-update-token]: https://github.blog/changelog/2022-05-03-github-actions-prevent-github-actions-from-creating-and-approving-pull-requests/
[license]: LICENSE
[logo-elixir]: images/logo-elixir.svg
[logo-elixir-cloud-aai]: images/logo-elixir-cloud-aai.svg
[poetry-org]: https://python-poetry.org/
[poetry-docs]: https://python-poetry.org/docs/cli/
[ruff]: https://docs.astral.sh/ruff
[ruff-formatter]: https://docs.astral.sh/ruff/formatter
[typos-docs]: https://pypi.org/project/typos/
[mypy-config]: https://mypy.readthedocs.io/en/stable/config_file.html
[sphinx-docs]: https://www.sphinx-doc.org/en/master/usage/configuration.html
[furo]: https://pradyunsg.me/furo/quickstart/
[rtd]: https://readthedocs.org/
[semver]: https://semver.org/
