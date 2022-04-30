# These are commands I should know, but for some reason have to Google them everytime I need them

## Update PIP

### Windows

  python -m pip install --upgrade pip

### Linux

  pip install --upgrade pip

## PIPENV - possibly bettern than pip with venv
pipfile = settings for pipenv, like which packages to isntall, where to download, and Python version.
pipfile.lock = Contains more info about what is installed, but should not be changed. 

Navigate to the project folder.

To activate the virtual environment:
  pipenvshell
To run a command from within the shell:
 
  pipenv run

To create a Virtual Environment or install a package, run:

  pipenv install [package]

Install a package only for the Development Environment:

  pipenv install --dev [package]

Install packages from requirements.txt file

  pipenv install -r [filename.txt]

## Create Virtual Environment

### Windows

  c:\Python35\python -m venv c:\path\to\myenv
  or
  python -m venv c:\path\to\myenv
  
### Linux

  python3 -m venv /path/to/new/virtual/environment
