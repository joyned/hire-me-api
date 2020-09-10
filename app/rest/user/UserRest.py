from flask import Blueprint, request

from app.service.user import UserService
from app.utils.response import Response

user_rest = Blueprint('user_service', __name__)


@user_rest.route('/api/users-profiles', methods=['GET'])
def get_users_profiles():
    return Response.execute(UserService.get_users_profiles, error_status_code=404)


@user_rest.route('/api/user/change-password', methods=['GET'])
def change_user_password():
    return Response.execute(UserService.get_users_profiles, request, error_status_code=400)