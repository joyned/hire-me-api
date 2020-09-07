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


@job_rest.route('/api/job/detail/<id>', methods=['POST'])
def get_details(id):
    return Response.execute(JobService.get_details, id, error_status_code=400)


@job_rest.route('/api/job/apply', methods=['POST'])
@token_validator(request)
def apply_job():
    return Response.execute(JobService.apply_job, error_status_code=400)


@job_rest.route('/api/job/applied', methods=['GET'])
@token_validator(request)
@cross_origin()
def get_applied_jobs():
    return Response.execute(JobService.get_applied_jobs, error_status_code=400)


@job_rest.route('/api/job/delete/<job_id>', methods=['POST'])
@token_validator(request)
def delete_apply_to_job(id):
    return Response.execute(JobService.delete_apply_to_job, id, error_status_code=400)
