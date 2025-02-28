# This Makefile was done using 'domake'
# Generated at 28/02/2025


# =================================================================================== #
# HELPERS
# =================================================================================== #

## help: print this help message
.PHONY: help
help:
	@echo 'Usage:'
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' | sed -e 's/^/ /'

.PHONY: confirm
confirm:
	@echo -n 'Are you sure? [y/N] ' && read ans && [ $${ans:-N} = y ]

# =================================================================================== #
# COMMANDS
# =================================================================================== #

## run: run the python program
.PHONY: run
run: 
	@venv/bin/python .
	

## py/version: show the python version installed in the virtual environment
.PHONY: py/version
py/version: 
	@venv/bin/python -V
	

## install: install a python package `name=<package>` in the virtual environment
.PHONY: install
install: 
	@venv/bin/python -m pip install ${name}
	

## uninstall: uninstall a python package `name=<package>` in the virtual environment
.PHONY: uninstall
uninstall: 
	@venv/bin/python -m pip uninstall ${name}
	

## req/set: creates/updates a requirements.txt file for the project
.PHONY: req/set
req/set: 
	@venv/bin/pip3 freeze > requirements.txt
	

## req/install: install python dependencies according to requirements.txt file for the project
.PHONY: req/install
req/install: 
	@venv/bin/python -m pip install -r requirements.txt

