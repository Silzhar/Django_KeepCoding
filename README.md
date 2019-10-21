# Django_KeepCoding

## Create virtual environment :

1. virtualenv env

2. source env/bin/activate

## Run project in terminal (create)

- $ django-admin.py startproject djangoProject


## Run project (web)

- $ python manage.py migrate  (initialize the database Django)

- $ python manage.py runserver  (start the development server)

### Create APP

- $ python manage.py startapp <name>
(add to the tuple INSTALLED_APPS in settings.py)

Example :  $ python manage.py startapp users