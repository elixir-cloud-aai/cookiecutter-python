import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
MODULE_NAME = '{{ cookiecutter.project_slug }}'
PROJECT_REGEX = r'^[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*$'
PROJECT_NAME = '{{ cookiecutter.project_name }}'

if not re.match(MODULE_REGEX, MODULE_NAME):
  print(
    f'ERROR: The project slug ({MODULE_NAME}) is not a valid Python module name.'
  )
  sys.exit(1)

if not re.match(PROJECT_REGEX, PROJECT_NAME):
  print(
    f'ERROR: The project name ({PROJECT_NAME}) is not valid.'
  )
  sys.exit(1)
