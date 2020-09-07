from flask import Blueprint, request

from app.service.register import RegisterService
from app.utils.response import Response

register_rest = Blueprint('register_service', __name__)


@register_rest.route('/api/register', methods=['POST'])
def register():
    return Response.execute(RegisterService.register, request, error_status_code=406)
