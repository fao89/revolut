from marshmallow import fields
from flask_marshmallow import Marshmallow
from revolut.models import User

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    username = fields.Str(required=True)
    password = fields.Str(required=True)