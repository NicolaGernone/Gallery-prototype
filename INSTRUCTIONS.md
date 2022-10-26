<img align="left"  width="150" height="150" src=".github/rviewer_logo--dark.png" />

## Rviewer skeleton: Python, Django & PostgreSQL

[![Twitter](https://img.shields.io/badge/rviewer__-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/Rviewer_/)

<br/>

This repository is a Python skeleton with Django & PostgreSQL designed for quickly getting started developing an API.
Check the [Getting Started](#getting-started) for full details.

## Technologies

* [Python 3.9](https://www.python.org/downloads/release/python-390/)
* [Django](https://docs.djangoproject.com/en/4.0/releases/4.0/)
* [Django REST framework](https://www.django-rest-framework.org/)
* [Poetry](https://python-poetry.org/)
* [Coverage](https://coverage.readthedocs.io/en/6.3.1/)
* [Docker](https://www.docker.com/)
* [Make](https://www.gnu.org/software/make/manual/make.html)

## Getting Started

Within the [Makefile](Makefile) you can handle the entire flow to get everything up & running:

1. Install `make` on your computer, if you do not already have it.
2. Build the Docker image: `make build`
3. Migrate any DB pending task: `make migrate`
4. Start the application: `make up`

As you could see on the [Makefile](Makefile) script, you could just avoid those steps and just execute `make up`, as **
build** and **migrate** are dependants of it.

Go to `http://127.0.0.1:5050/ping` to see that everything is up & running!

## Overview

This skeleton is split into two main folders:

### APP

This folder contains the main Django configuration. You will find there the core files to get the API up&running with
the basic Django settings parameters.

If you want to tweak or change anything of the configuration, this is the place!

### API

Here you will find the different files to expose your URLs & endpoints, but also some folders to start coding and
organize your code around
a [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html). 

You can use this as a starting point to continue with this architecture, or adapt it to your preferences. 

## Support

If you are having problems or need anything else, please let us know by
[raising a new issue](https://github.com/Rviewer-Challenges/skeleton-py-django/issues/new/choose).

## License

This project is licensed with the [MIT license](LICENSE).

--- 

<p align="center">
  Made with ❤️ by <a href="https://rviewer.io">Rviewer</a>
</p>
