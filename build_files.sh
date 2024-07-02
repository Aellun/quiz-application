#!/bin/bash

# Install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

# Install project dependencies
pip install -r requirements.txt

# Run Django collectstatic
python3 DjangoQuiz/manage.py collectstatic --noinput
