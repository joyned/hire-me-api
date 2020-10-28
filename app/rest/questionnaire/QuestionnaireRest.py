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
@token_validator(request)
def get_questionnaire_for_view(questionnaire_id):
    return Response.execute(QuestionnaireService.get_questionnaire_for_view, request, questionnaire_id,
                            error_status_code=403)


@questionnaire_rest.route('/api/questionnaire/get/response/<questionnaire_id>/<approval_id>', methods=['GET'])
@token_validator(request)
def get_questionnaire_for_response(questionnaire_id, approval_id):
    return Response.execute(QuestionnaireService.get_questionnaire_for_response, request, questionnaire_id, approval_id,
                            error_status_code=403)


@questionnaire_rest.route('/api/questionnaire/editable/<questionnaire_id>', methods=['GET'])
@token_validator(request)
def questionnaire_editable(questionnaire_id):
    return Response.execute(QuestionnaireService.questionnaire_editable, questionnaire_id, error_status_code=400)


@questionnaire_rest.route('/api/questionnaire/answer', methods=['POST'])
@token_validator(request)
def answer_questionnaire():
    return Response.execute(QuestionnaireService.answer_questionnaire, request, error_status_code=400)


@questionnaire_rest.route('/api/questionnaire/view/answers', methods=['POST'])
@token_validator(request)
def get_questionnaire_by_job_id_and_person_id():
    return Response.execute(QuestionnaireService.get_questionnaire_by_job_id_and_person_id, request,
                            error_status_code=403)


@questionnaire_rest.route('/api/questionnaire/correction', methods=['POST'])
@token_validator(request)
def correct_questionnaire():
    return Response.execute(QuestionnaireService.correct_questionnaire, request, error_status_code=400)
