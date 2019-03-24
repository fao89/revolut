import os
from flask import Flask
from flask_simplelogin import SimpleLogin
from revolut.rest import parser

SECRET = os.environ.get("SECRET_KEY")


def create_app(secret=SECRET):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secret
    SimpleLogin(app)
    app.register_blueprint(parser.blueprint)
    return app