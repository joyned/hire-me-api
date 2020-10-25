from flask import Blueprint, request

from app.security.TokenValidator import token_validator
from app.service.selectiveprocess import SelectiveProcessService
from app.utils.response import Response

selective_process_rest = Blueprint('selective.process', __name__)


@selective_process_rest.route('/api/selective/process', methods=['PUT'])
@token_validator(request)
def selective_process():
    return Response.execute(SelectiveProcessService.selective_process, request, error_status_code=403)


@selective_process_rest.route('/api/selective/process/list/simple', methods=['GET'])
@token_validator(request)
def list_selective_process_simple():
    return Response.execute(SelectiveProcessService.list_selective_process_simple, request, error_status_code=403)


@selective_process_rest.route('/api/selective/process/get/<selective_process_id>', methods=['GET'])
@token_validator(request)
def get_selective_process_by_id(selective_process_id):
    return Response.execute(SelectiveProcessService.list_selective_process, request, selective_process_id,
                            error_status_code=403)


@selective_process_rest.route('/api/selective/process/delete/<selective_process_id>', methods=['DELETE'])
@token_validator(request)
def delete_selective_process_by_id(selective_process_id):
    return Response.execute(SelectiveProcessService.delete_selective_process, selective_process_id,
                            error_status_code=403)


@selective_process_rest.route('/api/selective/process/editable/<selective_process_id>', methods=['GET'])
@token_validator(request)
def selective_process_editable(selective_process_id):
    return Response.execute(SelectiveProcessService.selective_process_editable, selective_process_id,
                            error_status_code=403)


@selective_process_rest.route('/api/selective/process/job/<job_id>', methods=['GET'])
@token_validator(request)
def get_selective_process_by_job_id(job_id):
    return Response.execute(SelectiveProcessService.get_selective_process_by_job_id, request, job_id,
                            error_status_code=404)


@selective_process_rest.route('/api/selective/process/candidates/<job_id>', methods=['GET'])
@token_validator(request)
def get_candidates(job_id):
    return Response.execute(SelectiveProcessService.get_candidates, job_id, error_status_code=403)


@selective_process_rest.route('/api/selective/process/job/candidate', methods=['POST'])
@token_validator(request)
def get_selective_process_by_job_and_candidate_id():
    return Response.execute(SelectiveProcessService.get_selective_process_by_job_and_candidate_id, request,
                            error_status_code=403)
