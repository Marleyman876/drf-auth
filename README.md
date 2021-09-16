# Feature Tasks and Requirements

## Features - Django

1. Add JWT Authentication to your API. [x]

2. Install needed libraries in project configuration and/or site settings. [x]

3. Keep any pre-existing authentication so DRF Browsable API still usable. [x]

4. Install needed libraries in project configuration and/or site settings.[x]

## Features - Docker

1. Create a boilerplate Dockerfile and docker-compose.yml so you don’t need to start from scratch each time. [x]
E.g. as a VS Code snippet, or a gist.

2. Switch to using Gunicorn instead of Django’s built in development server.[x]
    * mind the number of workers to avoid sluggishness

3. Warning You will run into styling issues when you switch over to Gunicorn.[x]
    * On Django side you’ll need to properly handle static files using Whitenoise.

