---------- Command Line ----------

> > django-admin startproject {PROJECT NAME}

> > django-admin startapp {APP NAME}

> > python manage.py runserver

Add 'BASE_DIR/templates' in settings.py - TEMPLATES
Add 'todo' in settings.py - INSTALLED_APPS

> > python manage.py makemigrations

> > python manage.py migrate

> > python manage.py createsuperuser

> > pip install gunicorn heroku

Add runtime.txt with language configuration
Add Procfile with
"web gunicorn {APP NAME}.wsgi:application --log-file -"

> > pip freeze > requirements.txt

Add below in settings.py
'import django_heroku',
'import dj_database_url',
'django_heroku.settings(locals())',

For localhost, use below for settings.py - DATABASES
{
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}

For Heroku, use 'dj_database_url.config()'

Add '*' (all users) in ALLOWED_HOSTS

> > heroku login
> > heroku create {APP NAME}

> > git init

> > git remote -v

> > git remote add {REMOTE NAME} {GIT URL}

> > heroku addons:create heroku-postgresql:hobby-dev

> > git add .

> > git commit -m "{MESSAGE}"

> > git push {REMOTE NAME} master

> > heroku run python manage.py makemigrations

> > heroku run python manage.py migrate

To remove git heroku remote
> > git remote rm {REMOTE NAME}