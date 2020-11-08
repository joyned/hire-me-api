from flask import Blueprint, request

from app.security.TokenValidator import token_validator
from app.service.password import PasswordService
from app.utils.response import Response

password_rest = Blueprint('password_rest', __name__)


@password_rest.route('/api/reset-password', methods=['POST'])
def reset_password():
    return Response.execute(PasswordService.reset_password, request, error_status_code=400)


@password_rest.route('/api/change-password', methods=['POST'])
@token_validator(request)
def change_password():
    return Response.execute(PasswordService.change_password, request, error_status_code=400)
