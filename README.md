# Website Link
http://fireshine.ai/

# SocialSite with APIs (mysite)
Backend python code


## Clone the project
Clone the project from Github:

    Project Root Directory: `/var/www`

    git clone remote url

## 1. Setup
### A. Docker setup for Development
Build a container

    docker compose build

Run bash in container (required* postgres and redis on host)

    docker run -it --env-file .env -v ./mysite:/webapp --network=host vaibhavbhwsr/fireshine_dev_image bash

To reconnect container

    docker attach <container-id>

note*: .env file is required

### B. Docker setup for Production

    docker compose -f docker-compose.prod.yaml up --build

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
