# Phonebook Web API for Android Assignment 2
To set up this project:
1. Install [Python 3.8](https://www.python.org/downloads/)
2. Check that you can [install packages with pip](https://packaging.python.org/tutorials/installing-packages/)
3. Install [pipenv](https://pypi.org/project/pipenv/) by running `pip install pipenv`
4. In the project folder, run `pipenv install` to install dependencies
5. Change `SQLALCHEMY_DATABASE_URI` in `setup_db.py` to [connect to your MySQL database](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format)
6. Run `pipenv run python setup_db.py` to create the database tables with sample data

To run this project, enter one of these in a shell:
* `pipenv run flask run`
* `pipenv run python app.py`
