# Python Cookiecutter Template

This is a Cookiecutter template for creating a Python project with Poetry,
including configurations for various project settings.

## Usage

1. **Install Cookiecutter** (if you haven't already):

```sh
pip install cookiecutter
```

2. **Generate a New Project**:

```sh
cookiecutter gh:elixir-cloud-aai/cookiecutter-python
```

## Configurations

### Package manager - Poetry

This project uses [Poetry](https://python-poetry.org/) as a package manager.
Check out the commands at the
[official documentation](https://python-poetry.org/docs/cli/).

### Linters and formatters - Ruff

To lint and format python code file, it uses
[Ruff](https://docs.astral.sh/ruff), the default configuration is set in the
`pyproject.toml` file.

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

To configure it to your needs, refer to the
[rules documentation](https://docs.astral.sh/ruff/rules/), and for formatter
configuration, refer to the
[configuration documentation](https://docs.astral.sh/ruff/formatter)

### Spell checker - typos

If you want to ignore certain words, add them to the `pyproject.toml` file,
under the `tool.typos.default.extend-words` key.

```toml
[tool.typos.default.extend-words]
mke = 'mke'
```

For further configration, refer to the [typos docs](https://pypi.org/project/typos/).

### Static type checker - mypy

Change the configuration in `mypy.ini` file, for further info refer to the
[mypy documentation](https://mypy.readthedocs.io/en/stable/config_file.html)

### Documentation - Sphinx

Configuration for Sphinx is in the `docs/source/conf.py` file, for further info refer
to the [Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/configuration.html).
The default configuration uses
[furo theme](https://pradyunsg.me/furo/quickstart/) and
[ReadTheDocs](https://readthedocs.org/) to host the documentation, you can
the config using `.readthedocs.yml` file.

### Testing - pytest and pytest-cov

Geneate a coverage report using `pytest-cov` and uploads it to codecov.io.

## CI/CD - GitHub Actions

Here are the GitHub Actions Secrets that need to be included in the repository
settings:

- `PYPI_PASSWORD`: The password for the PyPI account.
- `CODECOV_TOKEN`: The token for the codecov.io account.
- `AUTO_UPDATE_GITHUB_TOKEN`: The token for the create a PR to update the template.

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
versioning. Currently the service is in a pre-release stage, so changes to the
API, including breaking changes, may occur at any time without further notice.

## License

This project is distributed under the [Apache License 2.0][badge-license-url], a
copy of which is also available in [`LICENSE`][license].

## Contact

The project is maintained by [ELIXIR Cloud & AAI][elixir-cloud-aai], a Driver
Project of the [Global Alliance for Genomics and Health (GA4GH)][ga4gh], under
the umbrella of the [ELIXIR] [Compute Platform][elixir-compute].

To get in touch with use, please use one of the following routes:

- For filing bug reports, feature requests or other code-related issues, please
  make use of the project's
  [issue tracker](https://github.com/elixir-cloud-aai/cloud-components/issues).
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
[email]: mailto:alexander.kanitz@alumni.ethz.ch
[ga4gh]: https://ga4gh.org/
[license]: LICENSE
[logo-elixir]: images/logo-elixir.svg
[logo-elixir-cloud-aai]: images/logo-elixir-cloud-aai.svg
