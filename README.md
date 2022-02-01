# Cactus backend test

## Dependencies installation
Download/clone this repository, and go inside the directory
Then, install the necessary packages

```
sudo apt install python3-dev libpq-dev postgresql postgresql-contrib
```
## Virtual environment creation and pip installation
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## PostgreSQL and env variables
```
sudo su - postgres
psql
```
Inside the psql terminal type:
```
CREATE DATABASE cactus_db;
CREATE USER django WITH PASSWORD 'test_password';
ALTER USER django CREATEDB;
ALTER ROLE django SET client_encoding TO 'utf8';
ALTER ROLE django SET default_transaction_isolation TO 'read committed';
ALTER ROLE django SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE cactus_db TO django;

```
exit the terminal and the postgres user session
## Set environment variables
```
touch .env
echo "DB_NAME = \"cactus_db\"" >> .env
echo "DB_USER = \"django\"" >> .env
echo "DB_PASSWORD = \"test_password\"" >> .env
```
## Migrate DB and start server
```
.manage.py migrate
.manage.py runserver
```

To access the project go to http://127.0.0.1/login
