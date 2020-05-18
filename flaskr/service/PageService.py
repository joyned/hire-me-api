from flask import Blueprint, jsonify, request
from flaskr.repository.PageRepository import *
from flaskr.model.Pages import Pages
from flaskr.security.TokenValidator import token_validator

page_service = Blueprint('page_service', __name__)


@page_service.route('/api/pages/<user_id>', methods=['GET'])
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


@page_service.route('/api/permision-on-page', methods=['POST'])
@token_validator(request)
def check_permisson():
    data = request.get_json()
    user_id = data['userId']
    page = data['page']
    res = check_permission(user_id, page)
    if res is None:
        return jsonify({"message": 'Permission denied!'}), 401
    else:
        return jsonify({"load": True}), 200
