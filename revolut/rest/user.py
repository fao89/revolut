from flask import Blueprint, request, jsonify, current_app
from flask_simplelogin import login_required
from revolut.models import User
from revolut.serializers import UserSchema


bp_user = Blueprint('user', __name__)


@bp_user.route('/create-user', methods=['POST'])
def register():

    us = UserSchema()

    user, error = us.load(request.json)

    if error:
        return jsonify(error), 401

    user.gen_hash()

    current_app.db.session.add(user)
    current_app.db.session.commit()

    return us.jsonify(user), 201


@bp_user.route('/list-user', methods=['GET'])
@login_required(basic=True)
def list_user():
    result = User.query.all()
    us = UserSchema(many=True, only=('id', 'username'))
    return us.jsonify(result), 200


@bp_user.route('/delete-user/<user_id>', methods=['GET'])
@login_required(basic=True)
def delete_user(user_id):
    User.query.filter(User.id == user_id).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!!!')


@bp_user.route('/update-user/<user_id>', methods=['POST'])
@login_required(basic=True)
def update_user(user_id):
    bs = UserSchema()
    query = User.query.filter(User.id == user_id)
    query.update(request.json)
    if 'password' in request.json:
        query.first().gen_hash()
    current_app.db.session.commit()
    return bs.jsonify(query.first())

