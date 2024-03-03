# ACTA Map

## Url
https://subway-accessibility-3839bd01e088.herokuapp.com

## how to dev

### first time

- copy `.env.example` to `.env` and fill out the values
- create a database locally (on macs, I suggest the [Postgres app]([url](https://www.pgadmin.org)) and [Postico]([url](https://eggerapps.at/postico2/)))
- create a virtualenv - `python3 -m venv venv`
- activate it - `source venv/bin/activate`
- install dependencies - `pip install -r requirements.txt`
- run `python manage.py load_subway_data`
- setup vite/frontend tooling:

```bash
cd mainmap/static_src
npm install
```

### every time

- activate the virtualenv - `source venv/bin/activate`
- run the server - `python manage.py runserver`
- ALSO, in a separate terminal, run the tailwind watcher: `./bin/tailwind-watch.sh`
- ALSO, in another terminal, cd into the vite-managed javascript code directory and start the server there:

```bash
cd mainmap/static_src
npm run dev
```
