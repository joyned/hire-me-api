from flask import jsonify, request

import app.repository.job.JobRepository as JobRepository
from app.model.context.HireMeContext import HireMeContext
from app.model.job.JobFilter import JobFilter
from app.model.job.Job import Job
from app.model.job.JobBenefit import JobBenefit
from app.utils.response import Response


def save_new_job():
    return jsonify("working!")


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
    return job_list


def filter_jobs():
    data = request.get_json()

    job_filter = JobFilter()
    job_filter.job = data.get('job')
    job_filter.localization = data.get('localization')

    job_list = []

    result = JobRepository.filter_jobs(job_filter)

    for row in result:
        job = Job()
        job.id = row[0]
        job.title = row[1]
        job.city = row[2]
        job.state = row[3]
        job.country = row[4]
        job.description = row[5]
        job_list.append(job.serialize())
    return job_list


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

    for row in JobRepository.get_job_benefits(job.id):
        job_benefit = JobBenefit()
        job_benefit.job_id = row[0]
        job_benefit.benefit = row[1]
        job.job_benefits.append(job_benefit.serialize())

    return job.serialize()


# TODO: REVIEW THE RETURN
def apply_job():
    context = HireMeContext()
    context.build(request)

    data = request.get_json()
    job = data['jobId']

    JobRepository.apply_to_job(context.person_id, job)
    return {'message': 'Applied successfully.'}


def check_if_person_are_applied_to_job(job_id):
    context = HireMeContext()
    context.build(request)

    result = JobRepository.check_if_person_are_applied_to_job(context.person_id, job_id)

    if result is None:
        return False
    
    return True


def get_applied_jobs():
    context = HireMeContext()
    context.build(request)

    job_list = []
    for row in JobRepository.get_applied_jobs(context.person_id):
        job = Job()
        job.id = row[0]
        job.title = row[1]
        job.city = row[2]
        job.state = row[3]
        job.country = row[4]
        job_list.append(job.serialize())
    return job_list


# TODO: THIS METHOD NEEDS TO BE REVIEWED, IS NOT GOOD DELETE SOMETHING FROM DATABASE, NEED TO CONSIDER CREATE A FLAG
#  TO SET INACTIVE. IT NEEDS TO REVIEW THE RETURN TOO.
def delete_apply_to_job(job_id):
    context = HireMeContext()
    context.build(request)

    JobRepository.delete_apply_to_job(context.person_id, job_id)
    return Response.ok({'message': 'Deleted successfully.'})
