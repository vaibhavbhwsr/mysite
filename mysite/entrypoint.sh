#!/bin/sh

# Function to display verbose messages
verbose() {
    echo "======> $@ - $(date '+%Y-%m-%d %H:%M:%S')"
}

# Wait for PostgreSQL to become available
verbose "Waiting for PostgreSQL to start..."
while ! nc -z db 5432; do
    verbose "PostgreSQL is not yet available. Retrying in 0.1 seconds..."
    sleep 0.1
done
verbose "PostgreSQL is now available."

# Run Django management commands
verbose "Collecting static files..."
python manage.py collectstatic --no-input

verbose "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Start the Django application with Gunicorn and Daphne
verbose "Starting Gunicorn..."
gunicorn mysite.wsgi:application --bind 0.0.0.0:8000 &

verbose "Starting Daphne..."
daphne -b 0.0.0.0 -p 8001 mysite.asgi:application &

# Wait for background processes to finish
wait
