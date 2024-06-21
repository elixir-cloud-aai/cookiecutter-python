# This Makefile assumes, that dependencies are installed and if virtualenv
# is used, it is activated.
default: help

.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo "Available targets:"
	@echo "	\033[1mdocs \033[37m(d\033[0m)"
	@echo "		\033[36mAutogenerate docs for {{ cookiecutter.project_slug}}.\033[0m"

.PHONY: docs
docs:
	@echo "Generating documentation..."
	@sphinx-apidoc -f -o docs/pages python_cookiecutter/
	@cd docs && make html
	@echo "\n++++++++++++++++++++++++++Summary+++++++++++++++++++++++++++++++++++\n"
	@echo "Documentation generated successfully."
	@echo "Open docs/_build/html/index.html in your browser."
	@echo "Or run open it with python as:"
	@echo "python -m http.server -d docs/build/html/"

.PHONY: d
d: docs
