#!/bin/bash
PYTHON_BIN=python3
if [ ! -e /usr/bin/python3 ]; then PYTHON_BIN=python; fi

PYTHON_VERSION=$($PYTHON_BIN --version | awk '{print $2}')
REQUIRED_VERSION="3.10"

function version_gt() { 
	[ "$(printf '%s\n' "$@" | sort -V | head -n 1)" != "$1" ] 
}

if version_gt "$REQUIRED_VERSION" "$PYTHON_VERSION"; then
	echo "Error: Python version 3.10 or greater is required"
	exit 1;
fi

if [ ! -e megatools -a ! -e /usr/bin/megatools ]; then
	echo -e "Error: Download Megatools and add it to your PATH\nError: https://megatools.megous.com/builds/builds/" 
	exit 1
fi

if [ ! -e venv ]; then
	$PYTHON_BIN -m venv venv
	source venv/bin/activate
	pip install unofficial-xitroo-api==0.9
	pip install requests
	pip install pyside6
else
	source venv/bin/activate
fi
python Main.py
