#!/bin/bash
# Build the project
echo "Building the project..."

# Activate the virtual environment
# source venv/bin/activate

# Use the full path to manage.py
FULL_PATH_TO_MANAGE_PY="quiz-application/manage.py"

# Now proceed with the rest of the script
python3.9 -m pip install -r requirements.txt

echo "Make Migration..."
$FULL_PATH_TO_MANAGE_PY makemigrations --noinput
$FULL_PATH_TO_MANAGE_PY migrate --noinput

echo "Collect Static..."
$FULL_PATH_TO_MANAGE_PY collectstatic --noinput --clear
