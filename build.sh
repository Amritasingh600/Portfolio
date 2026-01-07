#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate

# Load initial data if this is the first deployment
python -c "
from portfolio.models import Profile
if not Profile.objects.exists():
    exec(open('load_data.py', encoding='utf-8').read())
    print('Initial data loaded!')
else:
    print('Data already exists, skipping load_data.py')
"
