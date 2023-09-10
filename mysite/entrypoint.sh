#!/bin/sh

while ! nc -z db 5432; do
    echo "Waiting for postgres..."
    sleep 0.1
done
echo "PostgreSQL started ..."

python manage.py makemigrations
python manage.py migrate

exec "$@"
