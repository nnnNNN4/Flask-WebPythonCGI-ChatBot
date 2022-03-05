#!/bin/bash

cd /Flask-Project-1/src
npm run watch &

cd /Flask-Project-1
flask db upgrade
flask run --port 8080 --host 0.0.0.0