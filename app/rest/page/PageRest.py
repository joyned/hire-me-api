from flask import Blueprint, request

from app.security.TokenValidator import token_validator
from app.service.page import PageService
from app.utils.response import Response

page_rest = Blueprint('page_service', __name__)


@page_rest.route('/api/pages/', methods=['GET'])
@token_validator(request)
def get_pages():
    return Response.execute(PageService.get_pages_by_request, request, error_status_code=400)


@page_rest.route('/api/permision-on-page', methods=['POST'])
@token_validator(request)
def check_permisson():
    return Response.execute(PageService.check_permisson, request, error_status_code=403)


@page_rest.route('/api/page-register', methods=['POST'])
@token_validator(request)
def register_page():
    return Response.execute(PageService.register_page, request, error_status_code=403)
