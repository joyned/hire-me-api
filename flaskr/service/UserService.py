import yaml
from flask import Blueprint, jsonify

from flaskr.repository import UserRepository
from flaskr.response import AbstractResponse

app_config = yaml.load(open('app_config.yml'))
user_service = Blueprint('user_service', __name__)


@user_service.route('/api/users-profiles', methods=['GET'])
def get_users_profiles():
    def func():
        users_profiles = []
        for row in UserRepository.get_users_profiles():
            user_profile = {
                'id': row[0],
                'constante': row[1]
            }
            users_profiles.append(user_profile)
        return users_profiles

    response = AbstractResponse
    response.do = func
    res = response.execute()
    return res.data
