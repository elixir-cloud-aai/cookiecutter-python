"""Unit tests for the __init__.py file."""

from pathlib import Path

import pytest


@pytest.fixture
def init_file_exists():
    """Check if the __init__.py file exists."""
    path_to_init_file = (
        Path(__file__).parents[2] / "{{ cookiecutter.project_slug }}" / "__init__.py"
    )
    assert path_to_init_file.exists(), f"File {path_to_init_file} does not exist."
