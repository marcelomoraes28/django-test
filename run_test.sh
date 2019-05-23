#!/bin/bash

if [ -d "venv" ]; then
  echo "Active virtualenv"
  source venv/bin/activate
else
   echo "venv does not exist, let's create it"
   python3 -m venv ./venv
   source venv/bin/activate
fi
echo "Install test dependencies"
pip install -r requirements_test.txt
pip install -r requirements.txt
echo "Running tests"
cd happiness
python manage.py test
