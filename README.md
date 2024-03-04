# Website Link
http://fireshine.tk/

# SocialSite with APIs (mysite)
Backend python code


## Clone the project
Clone the project from Github:

    Project Root Directory: `/var/www`

    git clone remote url


## 1. Docker setup
    Install docker and docker compose (or) docker desktop
    docker compose build
    docker compose up
    docker exec -it app webapp_mysite_container /bin/bash
    ./manage.py makemigration
    ./manage.py migrate
    ./manage.py createsuperuser

    To Recreate containers: docker compose up --force-recreate

    note*: setting.ini required
    

## 2. Virtual Environment Setup
Create Virtualenv Folder

    virtualenv --python=python3.8 Project_dir/.venv


Activate Environment:

    source project_venv/bin/activate

Install Packages:

    pip install -r mysite/requirements.txt

## Create settings.ini file in settings folder
    See example.ini

## Apply database migrations
    note*: create postgres database named mysitedb then run commands in environment.
    python3 manage.py makemigrations
    python3 manage.py migrate

## Create super user
    python3 manage.py createsuperuser

## notes*
    Use MODE=dev in local only else on server it requires static and media file and stop S3 bucket to use
