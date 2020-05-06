#!/bin/bash
echo "Instantiating virtualenv and running unit tests..."
mkdir -p virtualenv_temp
virtualenv -p python3 virtualenv_temp
source virtualenv_temp/bin/activate
echo "Activated Virtualenv."
echo "Installing dependencies..."
pip install -r requirements.txt
export ELASTICSEARCH_API_BASE_URL='http://local' 
coverage run -m pytest
coverage report -m
echo "Unit tests complete."
echo "Deactivating Virtualenv..."
deactivate
rm -rf ./virtualenv_temp
echo "Virtualenv deactivated."
echo "Local test complete."