from app.model.context.HireMeContext import HireMeContext
from app.model.selectiveprocess.JobSelectiveProcess import JobSelectiveProcess
from app.model.selectiveprocess.SelectiveProcess import SelectiveProcess
from app.model.selectiveprocess.SelectiveProcessStep import SelectiveProcessStep
from app.repository.selectiveprocess import SelectiveProcessRepository
from app.service.job import JobService
from app.service.selectiveprocessapproval import ApprovalSelectiveProcessService


def selective_process(request):
    data = request.get_json()

    selective_process_id = data.get('id')

    if selective_process_id is not None:
        delete_selective_process(selective_process_id)

    return {'seletiveProcessId': int(create_selective_process(request))}


def create_selective_process(request):
    context = HireMeContext()
    context.build(request)

    data = request.get_json()

    selective_process = SelectiveProcess()

    selective_process.title = data.get('title')

    selective_process.id = SelectiveProcessRepository.create_selective_process(selective_process, context)

    for row_step in data.get('steps'):
        step = SelectiveProcessStep()
        step.step_title = row_step.get('stepTitle')
        step.step_description = row_step.get('stepDescription')
        step.step_type = row_step.get('stepType')
        if not row_step.get('questionnaireId') == 0:
            step.questionnaire_id = row_step.get('questionnaireId')
        step.selective_process_id = selective_process.id
        step.order = row_step.get('order')

        SelectiveProcessRepository.create_selective_process_steps(step)

    return selective_process.id


def delete_selective_process(selective_process_id):
    if selective_process_editable(selective_process_id):
        SelectiveProcessRepository.delete_selective_process_steps(selective_process_id)
        SelectiveProcessRepository.delete_seletive_process(selective_process_id)
    else:
        raise Exception('selective.process.not.deletable')


def list_selective_process_simple(request):
    context = HireMeContext()
    context.build(request)

    selective_processes = []

    for row in SelectiveProcessRepository.list_selective_process(context):
        selective_process = SelectiveProcess()
        selective_process.id = row[0]
        selective_process.title = row[1]

        selective_processes.append(selective_process.serialize())

    return selective_processes


def list_selective_process(request, selective_process_id):
    context = HireMeContext()
    context.build(request)

    selective_process = SelectiveProcess()
    steps = []

    for row_process in SelectiveProcessRepository.list_selective_process_by_id(context, selective_process_id):
        selective_process.id = row_process[0]
        selective_process.title = row_process[1]

    for row_step in SelectiveProcessRepository.list_selective_process_step(selective_process_id):
        step = SelectiveProcessStep()
        step.id = row_step[0]
        step.step_title = row_step[1]
        step.step_description = row_step[2]
        step.step_type = row_step[3]
        step.questionnaire_id = row_step[4]
        step.selective_process_id = row_step[5]
        step.order = row_step[6]

        steps.append(step.serialize())

    selective_process.steps = steps

    return selective_process.serialize()


def selective_process_editable(selective_process_id):
    result = SelectiveProcessRepository.selective_process_editable(selective_process_id)
    if not len(result) == 0:
        return False
    else:
        return True


def get_selective_process_by_job_id(request, job_id):
    context = HireMeContext()
    context.build(request)

    job_selective_processes = []

    for row in SelectiveProcessRepository.get_selective_process_by_job_id(context.person_id, job_id):
        job_selective_process = JobSelectiveProcess()
        job_selective_process.step_title = row[0]
        job_selective_process.step_description = row[1]
        job_selective_process.step_type = row[2]
        job_selective_process.questionnaire_id = row[3]
        job_selective_process.order = row[4]
        job_selective_process.status = row[5]
        job_selective_process.id = row[6]

        job_selective_processes.append(job_selective_process.serialize())

    return {
        'jobTitle': JobService.get_job_title_by_id(job_id),
        'selectiveProcess': job_selective_processes
    }


def get_candidates(job_id):
    candidates = []
    for row in SelectiveProcessRepository.get_candidates(job_id):
        candidates.append({
            'candidateId': row[0],
            'candidateName': row[1],
            'applicationDate': row[2],
            'status': row[3]
        })

    return {'jobTitle': JobService.get_job_title_by_id(job_id), 'candidates': candidates}


def get_selective_process_by_job_and_candidate_id(request):
    data = request.get_json()

    person_id = data.get('personId')
    job_id = data.get('jobId')

    job_selective_processes = []

    for row in SelectiveProcessRepository.get_selective_process_by_job_id(person_id, job_id):
        job_selective_process = JobSelectiveProcess()
        job_selective_process.step_title = row[0]
        job_selective_process.step_description = row[1]
        job_selective_process.step_type = row[2]
        job_selective_process.questionnaire_id = row[3]
        job_selective_process.order = row[4]
        job_selective_process.status = row[5]
        job_selective_process.id = row[6]

        job_selective_process.can_approve = ApprovalSelectiveProcessService.can_approve(job_selective_process.id)

        job_selective_processes.append(job_selective_process.serialize())

    return {
        'jobTitle': JobService.get_job_title_by_id(job_id),
        'selectiveProcess': job_selective_processes
    }
