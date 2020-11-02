from flask import Blueprint, request

from app.security.TokenValidator import token_validator
from app.service.job import JobService
from app.utils.response import Response

job_rest = Blueprint('job_service', __name__)


@job_rest.route('/api/job/', methods=['PUT'])
@token_validator(request)
def save_job():
    return Response.execute(JobService.save_job, request, error_status_code=400)


@job_rest.route('/api/job/all', methods=['GET'])
def get_all_jobs():
    return Response.execute(JobService.get_all_jobs, error_status_code=404)


@job_rest.route('/api/job/filter', methods=['POST'])
def filter_jobs():
    return Response.execute(JobService.filter_jobs, request, error_status_code=400)


# TODO: Trocar para GET
@job_rest.route('/api/job/detail/<id>', methods=['POST'])
def get_details(id):
    return Response.execute(JobService.get_details, id, error_status_code=400)


@job_rest.route('/api/job/apply', methods=['POST'])
@token_validator(request)
def apply_job():
    return Response.execute(JobService.apply_job, request, error_status_code=400)


@job_rest.route('/api/job/personCanApply/<job_id>', methods=['GET'])
@token_validator(request)
def check_if_person_can_apply(job_id):
    return Response.execute(JobService.check_if_person_can_apply, job_id, request, error_status_code=403)


@job_rest.route('/api/job/applied-jobs', methods=['GET'])
@token_validator(request)
def get_applied_jobs():
    return Response.execute(JobService.get_applied_jobs, request, error_status_code=400)


@job_rest.route('/api/job/delete/<id>', methods=['POST'])
@token_validator(request)
def delete_apply_to_job(id):
    return Response.execute(JobService.delete_apply_to_job, id, request, error_status_code=400)


@job_rest.route('/api/job/jobs-by-user', methods=['GET'])
@token_validator(request)
def get_jobs_by_user_id():
    return Response.execute(JobService.get_jobs_by_user_id, request, error_status_code=401)


@job_rest.route('/api/job/applied-jobs/chart/30-days', methods=['GET'])
@token_validator(request)
def get_data_to_chart_from_30_days():
    return Response.execute(JobService.get_data_to_chart_from_30_days, request, error_status_code=403)


@job_rest.route('/api/job/candidates/<job_id>', methods=['GET'])
@token_validator(request)
def get_candidates_by_job_id(job_id):
    return Response.execute(JobService.get_candidates_by_job_id, job_id, error_status_code=403)


@job_rest.route('/api/job/status', methods=['POST'])
@token_validator(request)
def change_job_status():
    return Response.execute(JobService.change_job_status, request, error_status_code=403)
