# Modern TDD CI Python FastAPI example

Expanding on the code examples in the article "Modern Test-Driven Development in Python" by [jangia](https://github.com/jangia):

https://testdriven.io/blog/modern-tdd/


# Running with uvicorn

Set PYTHONPATH to top level directory:

$ export PYTHONPATH=`pwd`

Run from blog directory:

$ uvicorn app:app --reload

Initialise the database from top-level:

$ python blog/init_db.py



# Background

The blog article covers in some depth how to create a blog api and testing framework around it. So this is a fully functional and tested backend.

What it doesn't cover, though, are the basics of what is being implemented and what you can expect as you progress through the tutorial.

The backend is built on top of [SQLite](https://www.sqlite.org/index.html)

You can use SQLite browser to view creation of tables and data [SQLite Browser] (https://sqlitebrowser.org/)

# Running full test including e2e

In order to run full tests - run up the backend:

$ python blog/run.py

then ensure that the database is initialised:

$ python blog/init_db.py

And finally run the tests:

$ python -m pytest tests

# Running all non e2e tests

$ python -m pytest tests -m 'not e2e'