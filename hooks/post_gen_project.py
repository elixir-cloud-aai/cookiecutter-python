from pathlib import Path

project_slug = '{{cookiecutter.project_name_underscored}}'
path_to_workflows = Path.cwd() / '.github' / 'workflows'

create_main_file = '{{cookiecutter.add_script}}' == 'y'
create_pypi_release_ci = '{{cookiecutter.add_pypi_release_ci}}' == 'y'
create_dockerfile = '{{cookiecutter.add_docker_image}}' == 'y'

def remove(filepath):
    if Path.is_file(filepath):
        Path.unlink(filepath)

if not create_main_file:
    main_file_path = Path.cwd() / project_slug / 'main.py'
    remove(main_file_path)

if not create_pypi_release_ci:
    main_file_path = path_to_workflows / 'release_pypi.yaml'
    remove(main_file_path)

if not create_dockerfile:
    dockerfile_path = Path.cwd() / 'deployment' / 'images' / 'Dockerfile'
    remove(dockerfile_path)