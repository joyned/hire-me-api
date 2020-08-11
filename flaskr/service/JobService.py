from flask import Flask, jsonify, request, app
from flask import Blueprint
import flaskr.repository.JobRepository as JobRepository
from flaskr.model.HireMeContext import HireMeContext
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


# TODO: REVIEW THE RETURN
@job_service.route('/api/job-apply', methods=['POST'])
@token_validator(request)
def apply_job():
    context = HireMeContext()
    context.build(request)

    data = request.get_json()
    job = data['jobId']

    JobRepository.apply_to_job(context.candidate_id, job)
    return jsonify({'message': 'Applied successfully.'})


@job_service.route('/api/applied-jobs/', methods=['GET'])
@token_validator(request)
def get_applied_jobs():
    context = HireMeContext()
    context.build(request)

    job_list = []
    for row in JobRepository.get_applied_jobs(context.candidate_id):
        job = Job()
        job.id = row[0]
        job.title = row[1]
        job.city = row[2]
        job.state = row[3]
        job.country = row[4]
        job_list.append(job.serialize())
    return jsonify({"candidate_id": context.candidate_id, "applied_jobs": job_list})


# TODO: THIS METHOD NEEDS TO BE REVIEWED, IS NOT GOOD DELETE SOMETHING FROM DATABASE, NEED TO CONSIDER CREATE A FLAG
#  TO SET INACTIVE. IT NEEDS TO REVIEW THE RETURN TOO.
@job_service.route('/api/delete-applied-job/<jobId>', methods=['POST'])
@token_validator(request)
def delete_apply_to_job(jobId):
    context = HireMeContext()
    context.build(request)
    print(context.candidate_id)

    JobRepository.delete_apply_to_job(context.candidate_id, jobId)
    return jsonify({'message': 'Applied successfully.'})
