from passlib.hash import pbkdf2_sha512
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def gen_hash(self):
        self.password = pbkdf2_sha512.hash(self.password)

    def verify_password(self, password):
        return pbkdf2_sha512.verify(password, self.password)
