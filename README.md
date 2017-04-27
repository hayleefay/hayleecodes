# haylee.codes
A personal website that also serves up some data on migration trends.

## Getting started

* Create a `.env` which defines `DJANGO_SECRET`
* `brew install foreman`
* `brew install postgresql` (and follow instructions to launch with `launchctl`)
* `createdb migrant`
* `pip3 install -r requirements.txt`
* `python3 django_app/manage.py migrate`
* `forman start`
* Django app will be running at `localhost:5000`

### Seeding your database

Once your app is up and running, you will want some data. Run `python3 django_app/bilateral_data.py` to populate your database.
