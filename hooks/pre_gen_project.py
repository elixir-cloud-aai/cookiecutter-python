import requests
from typing import List
import re
import sys

# Attempt to import BeautifulSoup; handle if it's not installed
try:
    from bs4 import BeautifulSoup
    BS_AVAILABLE = True
except ImportError:
    BS_AVAILABLE = False

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
MODULE_NAME = '{{ cookiecutter.project_name_underscored }}'
PROJECT_REGEX = r'^[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*$'
PROJECT_NAME = '{{ cookiecutter.project_name_dashed }}'
PYTHON_VERSION = '{{ cookiecutter.python_version }}'


# Hardcoded list of Python versions as a fallback
HARDCODED_PYTHON_VERSIONS: List[str] = [
  "3.14",
  "3.13",
  "3.12",
  "3.11",
  "3.10",
  "3.9",
  "3.8"
]

def get_available_python_versions() -> List[str]:
  """
  Fetches the list of available Python versions.

  Scrapes the official Python website to retrieve a list of available Python 
  major, minor, and patch versions.

  Returns:
    List[str]: A sorted list of unique Python version strings 
      (e.g., ['3.11.4', '3.10.9']).
  
  Raises:
    SystemExit: Exits the program if there's an error fetching the Python 
      versions.
  """
  if BS_AVAILABLE is False:
    print(
      "NOTE: BeautifulSoup library is required to fetch Python versions."
      "Please install it by running 'pip install beautifulsoup4'.",
      "Using hardcoded Python versions as a fallback."
    )
    return HARDCODED_PYTHON_VERSIONS
  else:
    url: str = "https://www.python.org/downloads/"
    try:
      response: requests.Response = requests.get(url, timeout=10)
      response.raise_for_status()
    except requests.RequestException as e:
      print(f"Error fetching Python versions: {e}")
      sys.exit(1)
    
    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
    versions: List[str] = []
    
    # Extract all release-number spans
    release_number_spans: List[BeautifulSoup] = soup.find_all('span', class_='release-number')
    for span in release_number_spans:
      link = span.find('a')
      if link and link.text.startswith('Python'):
        text: str = link.text.strip()  # e.g., 'Python 3.11.3'
        parts: List[str] = text.split()
        if len(parts) == 2:
          version: str = parts[1]  # '3.11.3'
          versions.append(version)

    # Remove duplicates and sort versions in descending order
    unique_versions: List[str] = sorted(
      set(versions),
      key=lambda s: list(map(int, s.split('.'))),
      reverse=True
    )
    
    return unique_versions

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

if PYTHON_VERSION not in get_available_python_versions():
  print(
    f'ERROR: The Python version ({PYTHON_VERSION}) is not available.'
    "Please check https://www.python.org/downloads/ for the list of "
    "available versions."
  )
  sys.exit(1)