from flask import Blueprint, request

from app.security.TokenValidator import token_validator
from app.service.selectiveprocessapproval import ApprovalSelectiveProcessService
from app.utils.response import Response

approval_selective_process_rest = Blueprint('approval.selective.process', __name__)


@approval_selective_process_rest.route('/api/approval/selective/process/approve/<approved_step_id>', methods=['POST'])
@token_validator(request)
def approve(approved_step_id):
    return Response.execute(ApprovalSelectiveProcessService.approve, request, approved_step_id, error_status_code=403)


@approval_selective_process_rest.route('/api/approval/selective/process/reject/<approved_step_id>', methods=['POST'])
@token_validator(request)
def reject(approved_step_id):
    return Response.execute(ApprovalSelectiveProcessService.reject, approved_step_id, error_status_code=403)


@approval_selective_process_rest.route('/api/approval/selective/process/canApprove/<approved_step_id>', methods=['GET'])
@token_validator(request)
def can_approve(approved_step_id):
    return Response.execute(ApprovalSelectiveProcessService.can_approve, approved_step_id, error_status_code=403)