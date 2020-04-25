import jwt
import datetime
import yaml
from flask import Blueprint, jsonify, request, make_response
from flaskr.repository import UserRepository
from flaskr.model.User import User
from werkzeug.security import generate_password_hash, check_password_hash
import flaskr.repository.PageRepository as PageRepository

app_config = yaml.load(open('app_config.yml'))
user_service = Blueprint('user_service', __name__)


@user_service.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    hash_password = generate_password_hash(data.get('password'), method='sha256')
    check_user = check_if_user_exists(data.get('user'))
    if not check_user == "user_avaliable":
        message = register_error_message(check_user)
    else:
        UserRepository.insert_new_user(data.get('user'), hash_password)
        message = 'New user created.'

    return jsonify({'message': message})


def check_if_user_exists(user):
    result = UserRepository.check_if_user_exists_on_database(user)
    if result is not None:
        return 'user_already_exists'
    else:
        return 'user_avaliable'


def register_error_message(error):
    if error == "user_already_exists":
        return 'This user already exists in our system. Please, choose another.'


@user_service.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    request_user = data.get('user')
    request_pwd = data.get('password')
    if not (request_user == '' or request_user is None) or not (request_pwd == '' or request_pwd is None):
        return validate_user(request_user, request_pwd)

    return make_response('User and/or password are blank.', 401,
                         {'WWW-Authenticate': 'Base-realm="User and/or password are blank.'})


def validate_user(user, pwd):
    result = UserRepository.get_user_by_name(user)
    if result is not None:
        user = User()
        user.id = result[0]
        user.user = result[1]
        user.password = result[2]
        user.user_name = result[3]

        print(user.user_name)

        if check_password_hash(user.password, pwd):
            token = jwt.encode({
                'user_id': user.id,
                'user_name': user.user_name,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
            }, app_config['config']['key'])
            pages = PageRepository.get_all_pages_by_user_id(user.id)
            return jsonify({'user_id': user.id, 'user_name': user.user_name, 'time': datetime.datetime.utcnow(), 'token': token.decode('UTF-8'), 'pages': pages})
        else:
            return make_response('User and/or password are wrong.', 401,
                                 {'WWW-Authenticate': 'Base-realm="User and/or password are wrong.'})


