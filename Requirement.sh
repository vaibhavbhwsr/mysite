#!/bin/bash  

sudo apt-get install
sudo apt-get install virtualenv
cd ..
virtualenv --python=python3.8 .env/mysite
. .env/mysite/bin/activate
pip install django 
pip install psycopg2 
. .env/mysite/bin/activate
cd Latest-Project/mysite
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
. ../../.env/mysite/bin/activate
python manage.py runserver

