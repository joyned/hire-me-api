from flask import Blueprint, request

from app.security.TokenValidator import token_validator
from app.service.person import PersonService
from app.utils.response import Response

person_rest = Blueprint('person_service', __name__)


@person_rest.route('/api/person/get', methods=['GET'])
@token_validator(request)
def get_person_details():
    return Response.execute(PersonService.get_person_details, request, error_status_code=404)


@person_rest.route('/api/person/update', methods=['POST'])
@token_validator(request)
def update_person_details():
    return Response.execute(PersonService.update_candidate_details, request, error_status_code=400)


@person_rest.route('/api/person/professional/history', methods=['GET'])
@token_validator(request)
def get_professional_histories():
    return Response.execute(PersonService.get_professional_histories, request, error_status_code=404)


@person_rest.route('/api/person/professional/history/update', methods=['POST'])
@token_validator(request)
def update_professional_history():
    return Response.execute(PersonService.update_professional_history, request, error_status_code=400)
