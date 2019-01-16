

# mbari

mbari is built with [Python][0] using the [Django Web Framework][1].

mbari is a self-contained, revision-controlled repository of all code and documentation required to install, initialize, and run both a relational database backend (supported relational databases include PostgreSQL, MySQL/Mariadb, and sqlite) as well as a graphical user interface for data-entry and administration that is accessible through a web browser.  This solution is capable of running as a remote server (i.e., accessible over a network) or locally (i.e., on a single laptop or workstation).  The code repository includes a custom-designed database schema that facillitates data validation as it is entered in the user interface.

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv mbari`
    2. `$ . mbari/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
