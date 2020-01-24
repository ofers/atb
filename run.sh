#!/bin/bash

virtualenv venv/ -p /usr/bin/python3.6
source venv/bin/activate
pip install -r req.txt

uwsgi --ini webapp.ini
