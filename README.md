# ACTA Map

## Url
https://subway-accessibility-3839bd01e088.herokuapp.com

## how to dev

### first time

- copy `.env.example` to `.env` and fill out the values
- create a database locally (on macs, I suggest the Postgres app and Postico)
- create a virtualenv - `python3 -m venv venv`
- activate it - `source venv/bin/activate`
- install dependencies - `pip install -r requirements.txt`

### every time

- activate the virtualenv - `source venv/bin/activate`
- run the server - `python manage.py runserver`
