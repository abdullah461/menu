from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy


# create extention
db = SQLAlchemy()

# create app
def create_app():
    app = Flask(__name__)

    # secret key
    app.config['SECRET_KEY'] = 'abdullahiabubakar'

    # configure the SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    # initialize the app
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')


    return app