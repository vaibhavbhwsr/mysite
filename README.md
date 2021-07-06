# Facebook Clone (MySite)
Backend python code

## Clone the project
Clone the project from Github:

    Project Root Directory: `/var/www`
    
    git clone remote url


## Virtual Environment Setup
Create Virtualenv Folder

    virtualenv --python=python3.9 Project_dir/.venv


Activate Environment:

    source project_venv/bin/activate
   
Install Packages:
	
    pip install -r mysite/requirements.txt


## Apply database migrations
    note*: create postgres database named mysitedb then run commands in environment.
    python3 manage.py makemigrations 
    python3 manage.py migrate

## Create super user
    
    python3 manage.py createsuperuser


