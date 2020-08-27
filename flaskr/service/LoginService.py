import datetime

import jwt
import yaml
from flask import Blueprint, jsonify, request, make_response
from werkzeug.security import check_password_hash

import flaskr.repository.PageRepository as PageRepository
from flaskr.model.Person import Person
from flaskr.repository import LoginRepository

app_config = yaml.load(open('app_config.yml'))
login_service = Blueprint('login_service', __name__)


@login_service.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    request_email = data.get('email')
    request_pwd = data.get('password')
    if not (request_email == '' or request_email is None) or not (request_pwd == '' or request_pwd is None):
        return validate_email(request_email, request_pwd)

    return make_response('Email and/or password are blank.', 401,
                         {'WWW-Authenticate': 'Base-realm="User and/or password are blank.'})


def validate_email(email, pwd):
    result = LoginRepository.get_user_by_email(email)
    if result is not None:
        person = Person()
        person.user.id = result[0]
        person.user.email = result[1]
        person.user.password = result[2]
        person.user.user_profile_id = result[3]
        person.name = result[4]
        person.id = result[5]

        if check_password_hash(person.user.password, pwd):
            token = jwt.encode({
                'user_profile_id': person.user.user_profile_id,
                'user_id': person.user.id,
                'person_id': person.id,
                'person_name': person.name,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=100000)
            }, app_config['config']['key'])
            pages = PageRepository.get_all_pages_by_user_id(person.user.user_profile_id)
            return jsonify({'user_id': person.user.id, 'person_id': person.id, 'person_name': person.name,
                            'time': datetime.datetime.utcnow(), 'token': token.decode('UTF-8'), 'pages': pages})
        else:
            return make_response('Email and/or password are wrong.', 401,
                                 {'WWW-Authenticate': 'Base-realm="User and/or password are wrong.'})
