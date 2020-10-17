from flask import Blueprint, request

from app.security.TokenValidator import token_validator
from app.service.selectiveprocess import SelectiveProcessService
from app.utils.response import Response

selective_process_rest = Blueprint('selectiveprocess', __name__)


@selective_process_rest.route('/api/selective/process/create', methods=['POST'])
@token_validator(request)
def create_selective_process():
    return Response.execute(SelectiveProcessService.create_selective_process, request, error_status_code=403)


@selective_process_rest.route('/api/selective/process/list/simple', methods=['GET'])
@token_validator(request)
def list_selective_process_simple():
    return Response.execute(SelectiveProcessService.list_selective_process_simple, request, error_status_code=403)


@selective_process_rest.route('/api/selective/process/get/<selective_process>', methods=['GET'])
@token_validator(request)
def get_selective_process_by_id(selective_process):
    return Response.execute(SelectiveProcessService.list_selective_process, request, selective_process, error_status_code=403)