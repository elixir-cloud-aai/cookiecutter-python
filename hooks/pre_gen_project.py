import json
import re
import sys
import urllib.request

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
MODULE_NAME = '{{ cookiecutter.project_name_underscored }}'
PROJECT_REGEX = r'^[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*$'
PROJECT_NAME = '{{ cookiecutter.project_name_dashed }}'
PYTHON_VERSION = '{{ cookiecutter.python_version }}'


def fetch_versions_manifest() -> list:
  """Fetches the versions manifest from GitHub using urllib.
  
  Returns:
    list: A list of dictionaries with Python versions, or 
    an empty list if an error occurs.
  """
  manifest_url = "https://raw.githubusercontent.com/actions/python-versions/main/versions-manifest.json"
  
  try:
    with urllib.request.urlopen(manifest_url) as response:
      data = response.read()
      return json.loads(data)
  except Exception as e:
    print(f"Error fetching the versions manifest: {e}")
    return []
  
def valid_python_version() -> bool:
  """Check if the selected Python version is available in GitHub Actions Python versions.
  
  Returns:
    bool: True if the Python version is available, False otherwise.
  """
  data = fetch_versions_manifest()

  available_versions = {item["version"] for item in data}
  
  return PYTHON_VERSION in available_versions

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

if not valid_python_version():
  print(
    f'ERROR: The Python version ({PYTHON_VERSION}) is not available.'
    "Please check https://www.python.org/downloads/ for the list of "
    "available versions."
  )
  sys.exit(1)