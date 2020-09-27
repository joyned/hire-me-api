from flask import Blueprint, request
from flask_cors import cross_origin

from app.security.TokenValidator import token_validator
from app.service.job import JobService
from app.utils.response import Response

job_rest = Blueprint('job_service', __name__)


@job_rest.route('/api/job', methods=['POST'])
def save_new_job():
    return Response.execute(JobService.save_new_job, error_status_code=400)


@job_rest.route('/api/job/all', methods=['GET'])
def get_all_jobs():
    return Response.execute(JobService.get_all_jobs, error_status_code=404)


@job_rest.route('/api/job/filter', methods=['POST'])
def filter_jobs():
    return Response.execute(JobService.filter_jobs, error_status_code=400)


@job_rest.route('/api/job/detail/<id>', methods=['POST'])
def get_details(id):
    return Response.execute(JobService.get_details, id, error_status_code=400)


@job_rest.route('/api/job/apply', methods=['POST'])
@token_validator(request)
def apply_job():
    return Response.execute(JobService.apply_job, error_status_code=400)


@job_rest.route('/api/job/person-applied/<id>', methods=['GET'])
@token_validator(request)
def check_if_person_are_applied_to_job(id):
    return Response.execute(JobService.check_if_person_are_applied_to_job, id, error_status_code=400)


@job_rest.route('/api/job/applied-jobs', methods=['GET'])
@token_validator(request)
@cross_origin()
def get_applied_jobs():
    return Response.execute(JobService.get_applied_jobs, error_status_code=400)


@job_rest.route('/api/job/delete/<id>', methods=['POST'])
@token_validator(request)
def delete_apply_to_job(id):
    return Response.execute(JobService.delete_apply_to_job, id, error_status_code=400)


@job_rest.route('/api/job/jobs-by-user', methods=['GET'])
@token_validator(request)
def get_jobs_by_user_id():
    return Response.execute(JobService.get_jobs_by_user_id, request, error_status_code=401)


@job_rest.route('/api/job/applied-jobs/chart/30-days', methods=['GET'])
@token_validator(request)
def get_data_to_chart_from_30_days():
    return Response.execute(JobService.get_data_to_chart_from_30_days, request, error_status_code=401)