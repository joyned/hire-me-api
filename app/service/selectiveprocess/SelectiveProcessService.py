from app.model.context.HireMeContext import HireMeContext
from app.model.selectiveprocess.SelectiveProcess import SelectiveProcess
from app.model.selectiveprocess.SelectiveProcessStep import SelectiveProcessStep
from app.repository.selectiveprocess import SelectiveProcessRepository


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

        SelectiveProcessRepository.create_selective_process_steps(step)


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

        steps.append(step.serialize())

    selective_process.steps = steps

    return selective_process.serialize()
