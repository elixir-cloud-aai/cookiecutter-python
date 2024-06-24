import os

def remove_script_file():
  if '{{cookiecutter.add_script}}' != 'y':
    script_path = os.path.join(os.getcwd(), '{{cookiecutter.project_name}}', 'main.py')
    if os.path.exists(script_path):
        os.remove(script_path)

remove_script_file()
