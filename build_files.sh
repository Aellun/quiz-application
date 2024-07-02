#!/bin/bash

# Install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

# Add pip to PATH
export PATH=/python312/bin:$PATH

# Install project dependencies
pip install -r requirements.txt

# Run Django collectstatic
python3 manage.py collectstatic --noinput
