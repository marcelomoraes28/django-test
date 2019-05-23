#!/bin/bash

if [ -d "venv" ]; then
  echo "Active virtualenv"
  source venv/bin/activate
else
   echo "venv does not exist, let's create it"
   python3 -m venv ./venv
   source venv/bin/activate
fi

echo 'Install dependencies'
pip install -r requirements.txt
echo 'Installing assets dependencies'
npm install --prefix ./happiness/static bootstrap@4.3.1 jquery@3.4.1 chart.js@2.8.0 popper.js@1.15.0
echo 'Migrating the database'
python happiness/manage.py makemigrations
python happiness/manage.py migrate
python happiness/manage.py runserver
