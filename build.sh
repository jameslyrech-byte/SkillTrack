#!/usr/bin/env bash
set -o errexit


python -m pip install --upgrade pip
python -m pip install -r requirements.txt
# Apply the auth, session, and application migrations to Supabase before the
# release starts. Registering or logging in writes both user and session rows.
python manage.py migrate --noinput
python manage.py collectstatic --noinput
