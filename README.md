# EPICEVENTS

Openclassrooms - Parcours développement Python Projet 13

## Status

This project is under development.

## Description

Orange County Lettings is a start-up specialized in the real estate rental business. The start-up is in the midst of expansion in the United States.

This project consists in refactoring the website and deploying it on Heroku using a CI/CD pipeline and containerization.The website is available at the followig address: http://oc-lettings-2.herokuapp.com.

This project uses the following technologies:

* [Python](https://www.python.org) as the programming language
* [Django](https://www.djangoproject.com/) as a web framework
* [Pytest](https://pytest.org) and [Coverage](https://pypi.org/project/coverage/) for testing
* [Docker](https://www.docker.com) for containrization
* [CircleCI](https://www.circleci.com) for Continuous Integration
* [Heroku](https://www.heroku.com) for Deployment
* [Sentry](https://www.sentry.com) for monitoring

## Local Deployment

**Python 3** is required to run the website.

1. Clone this repository (or download the code [as a zip file](https://github.com/antoine71/OC_P13_OCLettings/archive/main.zip)), navigate to the root folder of the repository, create and activate a virtual environment, install project dependencies:

```shell
git clone https://github.com/antoine71/OC-P13_OCLettings.git
cd OC-P13_OCLettings
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

2. Run the server

```shell
$ python manage.py runserver
```

## Usage

The website is available from the following address:

```
http://localhost:8000/
```

## Administration

The application comes with an administration site.

```
http://localhost:8000/admin/
```

Only users with the status `superuser` can log in to the admin site.

The database comes with a pre-configured superuser account:
username: `admin`
password: `Abc1234!`

## Deployement using Heroku and Docker

1. Create a user account on [Heroku](http://www.heroku.com)
2. Download and install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
3. Download and install [Docker engine](https://docs.docker.com/engine/install/) according to your system requirement.
3. Create a new Heroku app (replace `<app_name>` by the name you choose)

```shell
heroku login
heroku apps:create <app_name>
````

4. Configure the Django secret key as an environment variable.

```shell
heroku config:set DJANGO_SECRET_KEY="<your_secret_key>" -a <app_name>
```

4. Navigate to the application root folder and build the container. The repository comes with a pre-configured Dockerfile. You can now build and push the container using Heroku CLI, then release it the Heroku.

It is preferable to use the command `docker build` rather than `heroku container:push` to build the container since it allows to specify the platform for which the container is build. Building the container from a different plateform using `heroku` command line (eg. arm64) may cause malfunctions.

```shell
docker build --platform linux/amd64 -t registry.heroku.com/<app_name>/web .
```

Login to the Heroku container registry:

```shell
heroku container:login
```

Push the container and activate it:

```shell
docker push registry.heroku.com/<app_name>/web
heroku container:release web -a <app_name>
```

5. You can now check the website from the following address: `https://<app_name>.herokuapp.com`.

## Deployment using CircleCI CI/CD Pipeline

