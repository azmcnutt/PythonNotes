# These are commands I should know, but for some reason have to Google them everytime I need them

## Update PIP

### Windows

  python -m pip install --upgrade pip

### Linux

  pip install --upgrade pip

## PIPENV - possibly bettern than pip with venv
pipfile = settings for pipenv, like which packages to install, where to download, and Python version.
pipfile.lock = Contains more info about what is installed, but should not be changed. 

### Navigate to the project folder.

### To activate the virtual environment:
  pipenvshell

### To run a command from within the shell:
 
  pipenv run

### To create a Virtual Environment or install a package, run:

  pipenv install [package]

### Install a package only for the Development Environment:

  pipenv install --dev [package]

### Install packages from requirements.txt file

  pipenv install -r [filename.txt]

### Remove a package:

  pipenv uninstall [package]

### Change Python version

First change version in pipfile then run:

  pipenv --python [version#]

### Delete and re-create the environment

  pipenv --rm
  pipend install

### Show environment location:

  pipenv --venv

### Check environment for security issues
  pipenv --check

### Update lock file for production:

  pipenv lock
  
Copy pipfile.lock to production environment, t hen run:
  
  pipenv install --ignore-pipfile

### .env files
  
.env files are automatically loaded to set environment cariables.


## Create Virtual Environment

### Windows

  c:\Python35\python -m venv c:\path\to\myenv
  or
  python -m venv c:\path\to\myenv
  
### Linux

  python3 -m venv /path/to/new/virtual/environment
