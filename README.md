# Minisite

A minimal dynamic website written in Python, based on FastAPI. 

## Why?

The primary reason to conceive this was to have a high-performance sidecar
service for WordPress.

It should provide a dynamic HTML page serving protected content without using
any bit of the WordPress PHP framework in order to provide availability even
if the main site croaks.

Instead, it will directly go to the WordPress database and authenticate users
against the ``wp_users`` table.

## Features

- Fits the container paradigm
- Just a single program to run
- Every setting can be configured through environment variables
- The HTML code is based on https://www.matuzo.at/blog/html-boilerplate/


## Installation

See Development » Installation.

## Usage

This service is configured through an ``.env`` file. You can have a look at
``.env.example`` for an example configuration.

When directly invoking the program, just run
```shell
minisite
```

When preferring Docker, invoke
```shell
docker-compose up
```


## Development

### Requirements

- Python 3
- Pip
- Poetry (Python Package Manager)


### Installation

Install package into virtual environment
```sh
python3 -m venv .venv
source .venv/bin/activate
make install
```

Run tests
```sh
make test
```

### Running on localhost

`make run`

## Deploy app

`make deploy`


### Automatic documentation

- Swagger: <http://localhost:8092/docs>
- Redocs: <http://localhost:8092/redoc>

### Project structure

Files related to application are in the `app` or `tests` directories.
Application parts are:

    app
    ├── api              - web related stuff.
    ├── core             - application configuration, startup events, logging.
    ├── models           - pydantic models for this application.
    ├── services         - logic that is not just crud related.
    └── main.py          - FastAPI application creation and configuration.
    │
    tests                - Software tests using pytest

The project layout has been created with ``cookiecutter gh:arthurhenrique/cookiecutter-fastapi``.
Thanks a stack, Arthur!
