#  Photo manager

![Workflow](https://github.com/Pavelkalininn/photo_manager/actions/workflows/main.yml/badge.svg)

## Description

###API provides ability:

1. Upload photos to authorized users.

   1.1 When uploading, you can specify various metadata: geolocation, description, names of people in the photo.

2. Display a list of photos, without metadata.

   2.2 Filter photos by date.
   
   2.3 Filter photos by geolocation (Latitude and Longitude).
   
   2.4 Filter photos by description.
   
   2.5 Filter photos by the person's name.

3. Get an ID photo with metadata.

4. Auto-completion to search for possible names of people present in the photos.

## Technologies

    Django==3.2.16
    django-filter==22.1
    djangorestframework==3.14.0
    djangorestframework-simplejwt==4.8.0
    djoser==2.1.0
    python-dotenv==0.21.0
    drf_extra_fields==3.4.1
    Pillow==9.4.0
    isort==5.11.4
    psycopg2-binary==2.8.6
    drf-yasg==1.21.4
    gunicorn==20.0.4
    flake8==5.0.4

## Env file template path:

[infra/example.env](./infra/example.env)

## Project run:

The DOCKER_USERNAME variable must be present in the Github secrets environment to run CI

## Project run:

### It is necessary to execute the commands in the infra folder to launch a project, apply migrations, create a superuser, load static, respectively:

Production version:

    docker-compose -f docker-compose_prod.yml up -d --build
    docker-compose -f docker-compose_prod.yml exec backend python manage.py migrate
    docker-compose -f docker-compose_prod.yml exec backend python manage.py createsuperuser
    docker-compose -f docker-compose_prod.yml exec backend python manage.py collectstatic --no-input

Develop version:

    docker-compose -f docker-compose_develop.yml up -d --build
    docker-compose -f docker-compose_develop.yml exec backend python manage.py migrate
    docker-compose -f docker-compose_develop.yml exec backend python manage.py createsuperuser
    docker-compose -f docker-compose_develop.yml exec backend python manage.py collectstatic --no-input

You need use docker-compose_develop.yml instead docker-compose_prod.yml for running application in development mode with open ports and running application without docker image and CI

## Documentation endpoints:

    /redoc/
   
    /swagger/

Admin panel available at:  

    /admin/

API available at:  

    /api/v1/

Names addition find endpoint:

   GET:
   
      /api/v1/faces/?name=a

   Response example:
   
      {
          "count": 3,
          "next": null,
          "previous": null,
          "results": [
              {
                  "id": 2,
                  "name": "Adam"
              },
              {
                  "id": 4,
                  "name": "Abby"
              },
              {
                  "id": 5,
                  "name": "Ali"
              }
          ]
      }


Stop containers command:

     docker-compose -f docker-compose_develop.yml stop

Stop and remove containers command:

     docker-compose -f docker-compose_develop.yml down -v

Production version of docker-compose file contains certbot for auto updating SSL certificate


Author: [__Pavel Kalinin__](https://github.com/Pavelkalininn)
