from flask import Blueprint, jsonify, request
from flaskr.auth import auth


user_service = Blueprint('user_service', __name__)


@user_service.route('/api/login-test', methods=['POST'])
def validate_login():
    data = request.get_json()
    valid = validate_login(data.get('user'), data.get('password'))
    return jsonify(build_login_response(valid))


@user_service.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = data.get('user')
    pwd = data.get('password')
    return auth.auth_user(user, pwd)


def build_login_response(valid):
    return {
        'success': valid
    }


def validate_login(user, pwd):
    if user == 'admin' and pwd == 'admin':
        return True
    else:
        return False

