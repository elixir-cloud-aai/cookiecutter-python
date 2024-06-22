# This Makefile assumes that dependencies are installed and, if a virtual environment
# is used, it is activated.
default: help

.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo "Available targets:"
	@echo "	\033[1m\033[35mclean-venv\033[0m \033[37m(cv)\033[0m"
	@echo "		\033[36mRemove virtual env.\033[0m"
	@echo "	\033[1m\033[35mdocs\033[0m \033[37m(d)\033[0m"
	@echo "		\033[36mGenerate project documentation.\033[0m"
	@echo "	\033[1m\033[35mformat-lint\033[0m \033[37m(fl)\033[0m"
	@echo "		\033[36mRun linter, formatter, and spellcheck.\033[0m"
	@echo "	\033[1m\033[35msecurity\033[0m \033[37m(s)\033[0m"
	@echo "		\033[36mRun security scan using bandit and safety.\033[0m"
	@echo "	\033[1m\033[35mtest\033[0m \033[37m(t)\033[0m"
	@echo "		\033[36mRun all the tests.\033[0m"
	@echo "	\033[1m\033[35mtype-check\033[0m \033[37m(tc)\033[0m"
	@echo "		\033[36mPerform type checking with mypy.\033[0m"
	@echo "	\033[1m\033[35mvenv\033[0m \033[37m(v)\033[0m"
	@echo "		\033[36mCreate a virtual environment.\033[0m"

.PHONY: docs
docs:
	@echo "Generating documentation..."
	@sphinx-apidoc -f -o docs/pages python_cookiecutter/
	@cd docs && make html
	@echo "\n++++++++++++++++++++++++++Summary+++++++++++++++++++++++++++++++++++\n"
	@echo "Documentation generated successfully."
	@echo "Open docs/_build/html/index.html in your browser."
	@echo "Or run it with python as:"
	@echo "python -m http.server -d docs/_build/html/"

.PHONY: d
d: docs

.PHONY: format-lint
format-lint:
	@echo "Running linter and formatter using ruff and typos..."
	@ruff format && ruff check --fix
	@typos .

.PHONY: fl
fl: format-lint

.PHONY: security
security:
	@echo "Running security scan using bandit and safety..."
	@safety check --full-report
	@bandit -c pyproject.toml -r {{ cookiecutter.project_slug }}/

.PHONY: s
s: security

.PHONY: test
test:
	@echo "Running tests using pytest..."
	@pytest tests/

.PHONY: t
t: test

.PHONY: type-check
type-check:
	@echo "Performing type check with mypy..."
	@mypy {{ cookiecutter.project_slug }}/

.PHONY: tc
tc: type-check

.PHONY: clean-venv
clean-venv:
	@echo "Removing venv..."
	@rm -rf .venv

.PHONY: cv
cv: clean-venv
