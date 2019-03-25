import os
from flask import Flask
from flask_migrate import Migrate
from flask_simplelogin import SimpleLogin
from revolut.rest import parser, user, login
from revolut.models import configure as config_db
from revolut.serializers import configure as config_ma

SECRET = os.environ.get("SECRET_KEY")


def create_app(secret=SECRET):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secret
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/revolut.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    config_db(app)
    config_ma(app)
    Migrate(app, app.db)
    login.configure(app)
    app.register_blueprint(parser.blueprint)
    app.register_blueprint(user.bp_user)
    return app