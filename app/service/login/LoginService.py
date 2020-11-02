import datetime

import jwt
from werkzeug.security import check_password_hash

import app.service.page.PageService as PageService
from app.model.person.Person import Person
from app.repository.login import LoginRepository
from app.utils.resource import ResourceUtil

app_config = ResourceUtil.get_resource_file('app_config.yml')


def login(request):
    data = request.get_json()
    request_email = data.get('email')
    request_pwd = data.get('password')
    if not (request_email == '' or request_email is None) or not (request_pwd == '' or request_pwd is None):
        return validate_email(request_email, request_pwd)
    else:
        raise Exception('Email and/or password are blank.')


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
        person.user.company_id = result[6]

        if check_password_hash(person.user.password, pwd):
            token = jwt.encode({
                'user_profile_id': person.user.user_profile_id,
                'user_id': person.user.id,
                'person_id': person.id,
                'person_name': person.name,
                'company_id': person.user.company_id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=100000)
            }, app_config['config']['key'])
            pages = PageService.get_pages(person.user.user_profile_id)
            return {'user_id': person.user.id, 'person_id': person.id, 'person_name': person.name,
                    'time': datetime.datetime.utcnow(), 'token': token.decode('UTF-8'), 'pages': pages}
        else:
            raise Exception('Email and/or password are wrong.')
    else:
        raise Exception('Email and/or password are wrong.')
