[![Tests](https://github.com/bownie/fairwinds-blog/actions/workflows/test.yml/badge.svg)](https://github.com/bownie/fairwinds-blog/actions/workflows/test.yml)
[![Linter](https://github.com/bownie/fairwinds-blog/actions/workflows/pylint.yml/badge.svg)](https://github.com/bownie/fairwinds-blog/actions/workflows/pylint.yml)

# Fairwinds Backend Python

Expanding on the code examples in the article "Modern Test-Driven Development in Python" by [jangia](https://github.com/jangia):

https://testdriven.io/blog/modern-tdd/

# Background

The blog article covers in some depth how to create a blog api and testing framework around it. So this is a fully functional and tested backend.

What it doesn't cover, though, are the basics of what is being implemented and what you can expect as you progress through the tutorial.

The backend is built on top of [SQLite](https://www.sqlite.org/index.html)

You can use SQLite browser to view creation of tables and data [SQLite Browser] (https://sqlitebrowser.org/)

# Running full test including e2e

In order to run full tests - run up the backend:

$ FLASK_APP=blog/app.py python -m flask run

then ensure that the database is initialised:

$ python blog/init_db.py

And finally run the tests:

$ python -m pytest tests

# Running all non e2e tests

$ python -m pytest tests -m 'not e2e'