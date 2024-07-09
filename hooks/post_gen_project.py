import os
from pathlib import Path
import shutil

project_slug = '{{cookiecutter.project_slug}}'

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

create_main_file = '{{cookiecutter.add_script}}' == 'y'

if not create_main_file:
    main_file_path = Path.cwd() / project_slug / 'main.py'
    remove(main_file_path)
