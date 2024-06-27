import os
from pathlib import Path

def remove_script_file():
  """Remove the console script init file.

  Removes the main.py file if the user does not want to add a script file.
  """
  if '{{cookiecutter.add_script}}' != 'y':
    script_path = Path.cwd() / '{{cookiecutter.project_name}}' / 'main.py'
    if os.path.exists(script_path):
        os.remove(script_path)

remove_script_file()
