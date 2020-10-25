from flask import jsonify

import app.repository.job.JobRepository as JobRepository
from app.model.context.HireMeContext import HireMeContext
from app.model.job.JobChart import JobChart
from app.model.job.JobFilter import JobFilter
from app.model.job.Job import Job
from app.model.job.JobBenefit import JobBenefit
from app.utils.response import Response


def save_job(request):
    context = HireMeContext()
    context.build(request)

    data = request.get_json()

    job = Job()
    job.title = data.get('title')
    job.city = data.get('city')
    job.state = data.get('state')
    job.description = data.get('description')
    job.salary = data.get('salary')
    job.selective_process_id = data.get('selectiveProcessId')

    for benefit in data.get('jobBenefits'):
        job_benefit = JobBenefit()
        values_view = benefit.values()
        value_iterator = iter(values_view)
        first_value = next(value_iterator)
        job_benefit.benefit = first_value
        job.job_benefits.append(job_benefit)

    job.company = context.company_id
    job.user_id = context.user_id

    if not data.get('id') == 0:
        job.id = data.get('id')
        JobRepository.delete_job_benefits(job.id)
        JobRepository.update_job(job)
    else:
        job.id = JobRepository.save_new_job(job)

    JobRepository.save_job_benefits(job)


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
        job.company = row[6]
        job_list.append(job.serialize())
    return job_list


def filter_jobs(request):
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
    job.company = result[7]
    job.selective_process_id = result[8]

    for row in JobRepository.get_job_benefits(job.id):
        job_benefit = JobBenefit()
        job_benefit.job_id = row[0]
        job_benefit.benefit = row[1]
        job.job_benefits.append(job_benefit.serialize())

    return job.serialize()


def apply_job(request):
    context = HireMeContext()
    context.build(request)

    data = request.get_json()
    job_id = data['jobId']

    try:
        JobRepository.apply_to_job(context.person_id, job_id)

        first_process_step = JobRepository.check_first_seletive_process_step_by_job_id(job_id)

        JobRepository.insert_first_step(context, job_id, first_process_step)
        return {'message': 'successful.apply'}
    except Exception as e:
        return {'message': 'fail.apply'}


def check_if_person_can_apply(job_id, request):
    context = HireMeContext()
    context.build(request)

    result = JobRepository.check_if_person_are_applied_to_job(context.person_id, job_id)

    if result is None:
        return True
    return False


def get_applied_jobs(request):
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
        job.description = row[5]
        job_list.append(job.serialize())
    return job_list


# TODO: THIS METHOD NEEDS TO BE REVIEWED, IS NOT GOOD DELETE SOMETHING FROM DATABASE, NEED TO CONSIDER CREATE A FLAG
#  TO SET INACTIVE. IT NEEDS TO REVIEW THE RETURN TOO.
def delete_apply_to_job(job_id, request):
    context = HireMeContext()
    context.build(request)

    JobRepository.delete_apply_to_job(context.person_id, job_id)
    return Response.ok({'message': 'Deleted successfully.'})


def get_jobs_by_user_id(request):
    context = HireMeContext()
    context.build(request)

    jobs = []

    for row in JobRepository.get_jobs_by_user_id(context.user_id):
        job = Job()
        job.id = row[0]
        job.title = row[1]
        if row[2] == 'T':
            job.status = True
        else:
            job.status = False
        jobs.append(job.serialize())

    return jobs


def get_data_to_chart_from_30_days(request):
    context = HireMeContext()
    context.build(request)

    job_chart = []

    for row in JobRepository.get_data_to_chart_from_x_days(31, context.company_id):
        chart = JobChart()
        chart.total = row[0]
        chart.date = row[1]
        chart.company_id = row[2]
        job_chart.append(chart.serialize())

    return job_chart


def get_candidates_by_job_id(job_id):
    candidates = []
    for row in JobRepository.get_candidates_by_job_id(job_id):
        candidates.append({
            'candidateName': row[0],
            'applicationDate': row[1]
        })
    return {'jobTitle': get_job_title_by_id(job_id), 'candidates': candidates}


def change_job_status(request):
    data = request.get_json()

    status = data.get('status')
    job_id = data.get('jobId')

    if status:
        status = 'T'
    else:
        status = 'F'

    JobRepository.change_job_status(status, job_id)


def get_job_title_by_id(job_id):
    return JobRepository.get_job_title_by_id(job_id)[0]
