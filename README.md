# simple-auth

> It's an app backend to authentication using Django Rest Framework
> Require python 3.6 o more

## Description

The goal of this project is to present a simple authentication app. It's create its as Web Service using Django Rest Framework; this is why it only contains the endpoint (CreateUser --> Register and Login).

## First Steps

* Clone this repo.

* To start firts you need install the requirements:

> pip install -r requirements.txt

* Migrate the django's models

> python manage.py migrate

* Run django server

> python manage.py runserver 0.0.0.0:8000

## Endpoint

```auth/register``` POST - Register user

```aauth/login```  POST log user in