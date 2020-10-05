# Video Club App

Video Club is a project created with Django 3.0.5 and Python 3.7.2. It also uses a PostgreSQL database.

## Installation

You will need to install PostgreSQL. After that open **psql** command line and type the following:

```bash
CREATE DATABASE deus;
CREATE USER deususer WITH ENCRYPTED PASSWORD 'deuspass';
ALTER ROLE deususer SET client_encoding TO 'utf8';
ALTER ROLE deususer SET default_transaction_isolation TO 'read committed';
ALTER ROLE deususer SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE deus TO deususer;
ALTER USER deususer CREATEDB;
\q
```

## Usage

You will need to migrate your database.

```python
manage.py migrate
```

And then start the application with:

```python
manage.py runserver 0.0.0.0:8000
```

You will probably need to create a superuser by:

```python
python manage.py createsuperuser
```

Note that there is also a custom management command available to help you create a custom user. You can do that by:

```python
python manage.py create_user
```

## Where to start
Base route of the application is

```python
http://127.0.0.1:8000/rent-store/
```

You will need to login first in order to be able to navigate the menus.

A **Swagger** documentation page is also available

```python
http://127.0.0.1:8000/swagger/
```

Tests are also available written with **pytest**.