# DJ Skeletor 2

DJ Skeletor is a skeleton Django project handy for quick bootstrapping of new
empty Django projects. It will help you get up and running with your project
in seconds.

The repository contains an empty, relocatable Django project with a selection
of useful Django application and setup for development, production and
automated test settings and environments.

DJ Skeletor makes it easy to follow the [12factor](http://12factor.net/)
approach (by specifying settings in environment variables or `.env` file),
while not mandating it.

DJ Skeletor 2 supports Django from version 1.7 onwards. If you need to use
Django 1.6 or earlier, use the
[original dj-skeletor](https://github.com/senko/dj-skeletor) instead.
DJ Skeletor 2 is rewritten from scratch to take advantage of the
new features available in the latest Django versions, such as built-in
database migrations and improved test runners.

### Quickstart

To start developing the project on the local machine, use the following
steps:

    # prepare the virtual environment
    mkvirtualenv --no-site-packages myenv

    # get the skeleton project
    git clone https://github.com/dobarkod/dj-skeletor2.git myproject
    cd myproject

    # use development settings
    export DJANGO_SETTINGS_MODULE=project.settings.dev

    # set up the development environment
    make dev-update

    # run your fully operational Django project
    python manage.py runserver

### Vagrant quickstart

To start using vagrant, use the following steps:

    # make sure you have the base vagrant image
    vagrant box add ubuntu/trusty64

    # create and provision the Vagrant box
    vagrant up

    # virtual machine with nginx, postgresql, gunicorn in production mode
    # is up and running, visit your site on http://localhost:8000/

### Batteries included

DJ Skeletor by default includes:

* Django 1.7
* Gunicorn 19.1.1
* Django Compressor 1.4
* Dj-static 0.0.6
* Vagrantfile (using official ubuntu/trusty64 image as base)
* Ansible playbook for setting up nginx and postgresql
* Heroku/foreman support (Procfile)

DJ Skeletor project structure is compatible with Heroku, so the project
can immediately be uploaded to a Heroku app, you just need to add the
heroku git remote and set up your Heroku credentials.
