from flask import Flask, jsonify, request, app
from flask import Blueprint
import flaskr.repository.JobRepository as JobRepository
from flaskr.model.Job import Job
from flaskr.security.TokenValidator import token_validator

job_service = Blueprint('job_service', __name__)


@job_service.route('/api/job', methods=['POST'])
def save_new_job():
    return jsonify("working!")


@job_service.route('/api/job/all', methods=['GET'])
def get_all_jobs():
    job_list = []
    for row in JobRepository.get_jobs():
        job = Job()
        job.id = row[0]
        job.title = row[1]
        job.city = row[2]
        job.state = row[3]
        job.country = row[4]
        job.description = row[5]
        job_list.append(job.serialize())
    return jsonify({"job_list": job_list})


@job_service.route('/api/job/detail/<id>', methods=['POST'])
def get_details(id):
    result = JobRepository.get_job_by_id(id)
    job = Job()
    job.id = result[0]
    job.title = result[1]
    job.city = result[2]
    job.state = result[3]
    job.country = result[4]
    job.salary = result[5]
    job.description = result[6]
    return jsonify(job.serialize())


@job_service.route('/api/job-apply')
@token_validator(request)
def apply_job():
    data = request.get_json()
    user = data['userId']
    job = data['jobId']
    JobRepository.apply_to_job(user, job)
    return jsonify({'message': 'Applied successfully.'})


@job_service.route('/api/applied-jobs')
@token_validator(request)
def get_applied_jobs():
    data = request.get_json()
    user = data['userId']
    job_list = []
    for row in JobRepository.get_applied_jobs(user):
        job = Job()
        job.id = row[0]
        job.title = row[1]
        job.city = row[2]
        job.state = row[3]
        job.country = row[4]
        job_list.append(job.serialize())
    return jsonify({"user": user, "applied_jobs": job_list})
