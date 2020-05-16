from flask import Blueprint, jsonify, request
from flaskr.repository.PageRepository import get_all_pages_by_user_id
from flaskr.model.Pages import Pages
from flaskr.security.TokenValidator import token_validator

page_service = Blueprint('page_service', __name__)


@page_service.route('/api/pages/<userId>', methods=['GET'])
@token_validator(request)
def get_pages(user_id):
    page_list = []
    res = get_all_pages_by_user_id(user_id)
    for row in res:
        page = Pages()
        page.id = row[0]
        page.constant = row[1]
        page.name = row[2]
        page_list.append(page.serialize())
    return jsonify({"userId": user_id, "pages": page_list})

