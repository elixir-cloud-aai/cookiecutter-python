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
