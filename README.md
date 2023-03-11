Install Prerequisites:

- Python: 3.8.+
- PostgreSQL: Version 12.+
- Python PIP
- docker

## Project Structure

Files related to application are in the ``app`` or ``tests`` directories.
Application parts are:

    app
    ├── api              - web related end points.
    │   ├── dependencies - dependencies for routes definition.
    │   └── routes       - web routes.
    ├── db               - db related stuff.
    │   └── repositories - all crud stuff.
    └── main.py          - FastAPI application creation and configuration.

## Local Development / Debugging

To run this application on a local dev machine, a few setup tasks are required:

1. [Create a virtual environment]
2. [Create a .env file]
5. [Setup a local postgres database]
7. [Debug and Test]

For the application to run, I just used docker version of PostgreSQL

### Postgresql -- Local version via docker

Use docker to run a local version of postgres:

````bash
docker run -d -p 0.0.0.0:5432:5432 --name postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres postgres:15  # launch docker contianer
````

Execute docker compose up -d.

This should bring up both the services DB and App and you can access the swagger docs on
localhost:8000/docs. If using this, change the DB host to "db" - the service name.

To use the dockerfile and execute the application, run the below commands.
docker build -t gutenberg .
docker run -p 8000:8000 gutenberg

This will render the swagger API in localhost:8000/docs and you can pass in the parameters as well as
number of results to see (pagination).

