[![Actions status](https://github.com/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}/workflows/CI/badge.svg)](https://github.com/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}/actions)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)
[![Python {{ cookiecutter.python_version }}](https://img.shields.io/badge/python-{{ cookiecutter.python_version}}-blue.svg)](https://www.python.org/downloads/release/python-311/)
[![GitHub contributors](https://img.shields.io/github/contributors/elixir-cloud-aai/{{ cookiecutter.project_slug }})](https://github.com/elixir-cloud-aai/TESK/graphs/contributors)
[![Ruff](https://img.shields.io/badge/linter%20&%20formatter-ruff-000000.svg)](https://docs.astral.sh/ruff/)

# {{ cookiecutter.project_slug }}

{{ cookiecutter.short_description }}

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
