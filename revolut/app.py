import os
from flask import Flask
from flask_simplelogin import SimpleLogin
from revolut.rest import parser


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
    SimpleLogin(app)
    app.register_blueprint(parser.blueprint)
    return app