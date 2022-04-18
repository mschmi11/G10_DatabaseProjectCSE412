# G10_DatabaseProjectCSE412
G10_DatabaseProjectCSE412


Based on tutorial here: https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application


Flask instructions:


install flask and psycopg2: 

pip install Flask psycopg2-binary


Login to Postgres session:

sudo -iu postgres psql


while in postgres:

CREATE DATABASE aircraft_db;

CREATE USER admin WITH PASSWORD 'admin';

GRANT ALL PRIVILEGES ON DATABASE aircraft_db TO admin;

\q


set user/password:

export DB_USERNAME="admin"

export DB_PASSWORD="admin"


run the init file to begin tables:

python3 init_db.py


running flask server:

export FLASK_APP=app.py

flask run


access the webpage at 127.0.0.1:5000


-------------------------------------------
File Descriptions:

init_db: start up tables and fill entries (right now has only one aircraft)

app.py: flask app for creating a server with the postgres table

templates: folder with html files

base.html: base html file

index.html: shows result of query

mapd3.js: use d3 to draw map

style.css: stylesheet for html







