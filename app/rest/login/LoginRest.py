from flask import Blueprint, request

from app.service.login import LoginService
from app.utils.response import Response

login_rest = Blueprint('login_service', __name__)


@login_rest.route('/api/login', methods=['POST'])
def login():
    return Response.execute(LoginService.login, request, error_status_code=401)
