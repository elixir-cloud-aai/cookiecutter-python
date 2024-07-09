{% if cookiecutter.add_script == 'y' %}
"""Entry point for python_cookiecutter."""


def main():
    """Main entry point for {{ cookiecutter.project_slug }}."""
    print("Hello from {{ cookiecutter.project_slug }}!")


if __name__ == "__main__":
    main()

{% endif %}
