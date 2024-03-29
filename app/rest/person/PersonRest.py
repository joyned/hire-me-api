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


@person_rest.route('/api/person/professional/history/get', methods=['GET'])
@token_validator(request)
def get_professional_histories():
    return Response.execute(PersonService.get_professional_histories, request, error_status_code=404)


@person_rest.route('/api/person/professional/history', methods=['PUT'])
@token_validator(request)
def professional_history():
    return Response.execute(PersonService.professional_history, request, error_status_code=400)


@person_rest.route('/api/person/professional/history/delete/<professional_history_id>', methods=['DELETE'])
@token_validator(request)
def delete_professional_history(professional_history_id):
    return Response.execute(PersonService.delete_professional_history, professional_history_id, error_status_code=400)


@person_rest.route('/api/person/abilities/get', methods=['GET'])
@token_validator(request)
def get_abilities():
    return Response.execute(PersonService.get_abilities, request, error_status_code=400)


@person_rest.route('/api/person/abilities', methods=['POST'])
@token_validator(request)
def insert_abilities():
    return Response.execute(PersonService.insert_ability, request, error_status_code=400)


@person_rest.route('/api/person/profile/<person_id>', methods=['GET'])
@token_validator(request)
def get_person_profile(person_id):
    return Response.execute(PersonService.get_person_profile, person_id, error_status_code=403)


@person_rest.route('/api/person/education/get', methods=['GET'])
@token_validator(request)
def get_person_education():
    return Response.execute(PersonService.get_person_education, request, error_status_code=400)


@person_rest.route('/api/person/education', methods=['PUT'])
@token_validator(request)
def person_education():
    return Response.execute(PersonService.person_education, request, error_status_code=400)


@person_rest.route('/api/person/education/delete/<person_education_id>', methods=['DELETE'])
@token_validator(request)
def delete_person_education(person_education_id):
    return Response.execute(PersonService.delete_person_education, person_education_id, error_status_code=400)
