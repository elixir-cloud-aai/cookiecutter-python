# NOTE: This Makefile assumes that dependencies are installed and, if a virtual
# environment is used, it is activated.

## Variables #################################################################

# NOTE: Define any variables here if needed in the future

## Documentation ##############################################################

default: help

.PHONY: help
help:
	@echo "\n++++ Usage: make [target] ++++\n"
	@echo "Available targets:"
	@echo "  \033[1m\033[35mclean-venv\033[0m \033[37m(cv)\033[0m"
	@echo "    \033[36mRemove the virtual environment.\033[0m"
	@echo "  \033[1m\033[35mdocs\033[0m \033[37m(d)\033[0m"
	@echo "    \033[36mGenerate project documentation.\033[0m"
	@echo "  \033[1m\033[35mformat-lint\033[0m \033[37m(fl)\033[0m"
	@echo "    \033[36mRun linter, formatter, and spellcheck.\033[0m"
	@echo "  \033[1m\033[35minstall\033[0m \033[37m(i)\033[0m"
	@echo "    \033[36mInstall all dependencies and {{ cookiecutter.project_slug }}.\033[0m"
	@echo "  \033[1m\033[35mprecommit-check\033[0m \033[37m(pc)\033[0m"
	@echo "    \033[36mRun all pre-commit checks.\033[0m"
	@echo "  \033[1m\033[35msecurity\033[0m \033[37m(s)\033[0m"
	@echo "    \033[36mRun security scans using bandit and safety.\033[0m"
	@echo "  \033[1m\033[35mtest\033[0m \033[37m(t)\033[0m"
	@echo "    \033[36mRun all tests.\033[0m"
	@echo "  \033[1m\033[35mtype-check\033[0m \033[37m(tc)\033[0m"
	@echo "    \033[36mPerform type checking with mypy.\033[0m"
	@echo "  \033[1m\033[35mvenv\033[0m \033[37m(v)\033[0m"
	@echo "    \033[36mCreate a virtual environment.\033[0m"

## Targets ####################################################################
# NOTE: Keep all the targets in alphabetical order for better readability.

.PHONY: clean-venv
clean-venv:
	@echo "\n++++ Removing the virtual environment ++++\n"
	@rm -rf .venv
	@echo "Virtual environment removed."

.PHONY: cv
cv: clean-venv

.PHONY: docs
docs:
	@echo "\n++++ Generating project documentation ++++\n"
	@sphinx-apidoc -f -o docs/pages python_cookiecutter/
	@cd docs && make html
	@echo "\n++++++++++++++++++++++++++ Summary +++++++++++++++++++++++++++++++++++\n"
	@echo "Documentation generated successfully."
	@echo "Open docs/_build/html/index.html in your browser."
	@echo "Or serve it locally using:"
	@echo "python -m http.server -d docs/_build/html/"

.PHONY: d
d: docs

.PHONY: format-lint
format-lint:
	@echo "\n++++ Running linter and formatter using ruff and typos ++++\n"
	@ruff format && ruff check --fix
	@typos .
	@echo "Linting and formatting completed."

.PHONY: fl
fl: format-lint

.PHONY: install
install:
	@echo "\n++++ Installing dependencies and {{ cookiecutter.project_slug }} ++++\n"
	@poetry install
	@echo "Installation completed."

.PHONY: i
i: install

.PHONY: precommit-check
precommit-check:
	@echo "\n++++ Running pre-commit checks ++++\n"
	@pre-commit run --all-files
	@echo "Pre-commit checks completed."

.PHONY: pc
pc: precommit-check

.PHONY: security
security:
	@echo "\n++++ Running security scans using bandit and safety ++++\n"
	@safety check --full-report
	@bandit -c pyproject.toml -r {{ cookiecutter.project_slug }}/
	@echo "Security scans completed."

.PHONY: s
s: security

.PHONY: test
test:
	@echo "\n++++ Running tests using pytest ++++\n"
	@pytest tests/
	@echo "Tests completed."

.PHONY: t
t: test

.PHONY: type-check
type-check:
	@echo "\n++++ Performing type checking with mypy ++++\n"
	@mypy {{ cookiecutter.project_slug }}/
	@echo "Type checking completed."

.PHONY: tc
tc: type-check

.PHONY: venv
venv:
	@echo "\n++++ Creating a virtual environment ++++\n"
	@python -m venv .venv
	@echo "\n++++++++++++++++++++++++++ Summary +++++++++++++++++++++++++++++++++++\n"
	@echo "Virtual environment created successfully."
	@echo "To activate the environment for this shell session, run:"
	@echo "source .venv/bin/activate"

.PHONY: v
v: venv
