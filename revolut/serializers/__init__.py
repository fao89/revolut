from flask_marshmallow import Marshmallow
from revolut.models import User

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    username = ma.auto_field()
    password = ma.auto_field()