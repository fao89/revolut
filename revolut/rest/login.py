from flask import current_app as app
from flask_simplelogin import SimpleLogin
from revolut.models import User
from revolut.serializers import UserSchema


def login_checker(user):
    username = user.get('username')
    password = user.get('password')
    if not username or not password:
        return False
    existing_user = user = User.query.filter_by(username=username).first()
    if not existing_user:
        return False
    if user.verify_password(password):
        return True
    return False


def create_user(username, password):
    if User.query.filter_by(username=username).first():
        raise RuntimeError(f'{username} already registered')
    
    us = UserSchema()
    user, error = us.load({'username': username,
            'password': password})

    user.gen_hash()
    app.db.session.add(user)
    app.db.session.commit()
    return User.query.filter_by(username=username).first()


def configure(app):
    """Adds login control"""
    SimpleLogin(app, login_checker=login_checker)