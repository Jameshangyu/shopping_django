# A shopping project in Python with Django
A python django drives a shopping project for purchasing items

It will be easy for buying the things which someone likes to own; Django follows MVC(Model-View-Controller) for code reusing.

## set up development environment
We could start to develop this project. Create a new folder 'shopping_django' and then use cd to get into this folder via terminal command line:

         pyenv local 3.7.0 # this sets the local version of python to 3.7.0
         python3 -m venv .venv # this creates the virtual environment for you
         source .venv/bin/activate # this activates the virtual environment
         pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.

We will use Django as our framework for our shopping application; We use next command line to install.

         pip install django

We would like to create the site using django admin tool. It is admin part for this application
        
         django-admin startproject mysite .

We will modify setting for this site, and we will do it by changing 'mysite/settings.py' to add package

         import os

Now go to the end of the file to add a line specifying the root directory for the static files.

         STATIC_ROOT = os.path.join(BASE_DIR, 'static')

Now we need to modify the 'ALLOWED_HOSTS' so that we can run the box url and configure the database.

         python3 manage.py migrate

## start running this server
We will use 'manage.py' to run this application by the command:

        python3 manage.py runserver 0.0.0.0:8000

It will show a rocket logo for success.

## Modeling the data



