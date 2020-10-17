from flask import Blueprint, request

from app.security.TokenValidator import token_validator
from app.utils.response import Response
from app.service.questionnaire import QuestionnaireService

questionnaire_rest = Blueprint('questionnaire_rest', __name__)


@questionnaire_rest.route('/api/questionnaire', methods=['PUT'])
@token_validator(request)
def questionnaire():
    return Response.execute(QuestionnaireService.questionnaire, request, error_status_code=400)


@questionnaire_rest.route('/api/questionnaire/delete/<questionnaire_id>', methods=['DELETE'])
@token_validator(request)
def delete_questionnaire(questionnaire_id):
    return Response.execute(QuestionnaireService.delete_questionnaire, questionnaire_id, error_status_code=400)


@questionnaire_rest.route('/api/questionnaire/list/simple', methods=['GET'])
@token_validator(request)
def list_questionnaires_simple():
    return Response.execute(QuestionnaireService.list_questionnaires_simple, request, error_status_code=403)


@questionnaire_rest.route('/api/questionnaire/get/<questionnaire_id>', methods=['GET'])
def get_questionnaire_for_view(questionnaire_id):
    return Response.execute(QuestionnaireService.get_questionnaire_for_view, request, questionnaire_id,
                            error_status_code=403)


@questionnaire_rest.route('/api/questionnaire/editable/<questionnaire_id>', methods=['GET'])
def questionnaire_editable(questionnaire_id):
    return Response.execute(QuestionnaireService.questionnaire_editable, questionnaire_id, error_status_code=4000)
