from flask import Flask

from revolut.rest import parser


def create_app():
    app = Flask(__name__)
    app.register_blueprint(parser.blueprint)
    return app