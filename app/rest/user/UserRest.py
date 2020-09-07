from flask import Blueprint

from app.service.user import UserService
from app.utils.response import Response

user_rest = Blueprint('user_service', __name__)


@user_rest.route('/api/users-profiles', methods=['GET'])
def get_users_profiles():
    return Response.execute(UserService.get_users_profiles, error_status_code=404)
