from app.model.context.HireMeContext import HireMeContext
from app.model.questionnaire.QuestionnaireQuestion import QuestionnaireQuestion
from app.model.questionnaire.Questionnaire import Questionnaire
from app.model.questionnaire.QuestionnaireQuestionOption import QuestionnaireQuestionOption
from app.repository.questionnaire import QuestionnaireRepository
from app.utils.response import Response


def questionnaire(request):
    data = request.get_json()

    questionnaire_id = data.get('id')

    if questionnaire_id is None:
        return {'questionnaire': int(create_questionnaire(request))}
    else:
        delete_questionnaire(questionnaire_id)
        return {'questionnaire': int(create_questionnaire(request))}


def create_questionnaire(request):
    data = request.get_json()

    questionnaire = Questionnaire()
    context = HireMeContext()
    context.build(request)

    questionnaire.title = data.get('title')

    for question in data.get('questionnaireQuestions'):
        questionnaire_question = QuestionnaireQuestion()
        questionnaire_question.question_title = question.get('questionTitle')
        questionnaire_question.question_help = question.get('questionHelp')
        questionnaire_question.answer_type = question.get('answerType')
        questionnaire_question.answer_time = question.get('answerTime')

        questionnaire.questionnaire_questions.append(questionnaire_question)

        for option in question.get('questionnaireQuestionOption'):
            question_option = QuestionnaireQuestionOption()
            question_option.option_title = option.get('optionTitle')
            questionnaire_question.questionnaire_question_options.append(question_option)

    return QuestionnaireRepository.create_questionnaire(context, questionnaire)


def delete_questionnaire(questionnaire_id):
    if questionnaire_editable(questionnaire_id):
        delete_options_by_questionnaire_id(questionnaire_id)
        delete_question_by_questionnaire_id(questionnaire_id)
        QuestionnaireRepository.delete_questionnaire(questionnaire_id)
    else:
        raise Exception('not.editable.questionnaire')


def delete_question_by_questionnaire_id(questionnaire_id):
    QuestionnaireRepository.delete_question_by_questionnaire_id(questionnaire_id)


def delete_options_by_questionnaire_id(questionnaire_id):
    QuestionnaireRepository.delete_option_by_questionnaire_id(questionnaire_id)


def list_questionnaires_simple(request):
    context = HireMeContext()
    context.build(request)

    questionnaires = []

    for questionnaire in QuestionnaireRepository.list_questionnaires_simple(context):
        quest = Questionnaire()

        quest.id = questionnaire[0]
        quest.title = questionnaire[1]
        quest.status = questionnaire[2] == 'T'

        questionnaires.append(quest.serialize())

    return questionnaires


def get_questionnaire(request, questionnaire_id, for_view):
    context = HireMeContext()
    context.build(request)

    questionnaire = Questionnaire()

    result = QuestionnaireRepository.get_questionnaire_by_id(context, questionnaire_id, for_view)
    questionnaire.id = questionnaire_id
    questionnaire.title = result[0]
    questionnaire.company_id = result[1]
    questionnaire.user_id = result[2]

    for row_question in QuestionnaireRepository.get_questionnaire_question_by_id(questionnaire.id):
        question = QuestionnaireQuestion()
        question.id = row_question[0]
        question.question_title = row_question[1]
        question.question_help = row_question[2]
        question.answer_type = row_question[3]
        question.questionnaire_answer = row_question[4]
        question.questionnaire_id = questionnaire_id

        questionnaire.questionnaire_questions.append(question.serialize())

        for row_option in QuestionnaireRepository.get_questionnaire_question_options_by_id(question.id):
            option = QuestionnaireQuestionOption()
            option.id = row_option[0]
            option.option_title = row_option[1]

            question.questionnaire_question_options.append(option.serialize())

    return questionnaire.serialize()


def get_questionnaire_for_response(request, questionnaire_id):
    return get_questionnaire(request, questionnaire_id, False)


def get_questionnaire_for_view(request, questionnaire_id):
    return get_questionnaire(request, questionnaire_id, True)


def get_questionnaire_by_job_id_and_person_id(request):
    context = HireMeContext()
    context.build(request)
    data = request.get_json()

    job_id = data.get('jobId')
    person_id = data.get('personId')
    questionnaire_id = data.get('questionnaireId')

    questionnaire = Questionnaire()

    result = QuestionnaireRepository.get_questionnaire_by_id(context, questionnaire_id, False)
    questionnaire.id = questionnaire_id
    questionnaire.title = result[0]
    questionnaire.company_id = result[1]
    questionnaire.user_id = result[2]

    for row_question in QuestionnaireRepository.get_questionnaire_by_job_id_and_person_id(job_id, person_id):
        question = QuestionnaireQuestion()
        question.id = row_question[0]
        question.question_title = row_question[1]
        question.question_help = row_question[2]
        question.answer_type = row_question[3]
        question.questionnaire_answer = row_question[4]
        question.answer_id = row_question[5]
        question.questionnaire_correct = row_question[6]
        question.questionnaire_id = questionnaire_id

        questionnaire.questionnaire_questions.append(question.serialize())

        for row_option in QuestionnaireRepository.get_questionnaire_question_options_by_id(question.id):
            option = QuestionnaireQuestionOption()
            option.id = row_option[0]
            option.option_title = row_option[1]

            question.questionnaire_question_options.append(option.serialize())

    return questionnaire.serialize()


def questionnaire_editable(questionnaire_id):
    result = QuestionnaireRepository.questionnaire_editable(questionnaire_id)
    if result == 1:
        return False
    else:
        return True


def answer_questionnaire(request):
    context = HireMeContext()
    context.build(request)

    data = request.get_json()

    approval_id = data.get('approvalId')
    questions = data.get('questionnaire').get('questionnaireQuestions')
    if QuestionnaireRepository.check_if_can_answer_questionnaire(approval_id) is None:
        for question in questions:
            questionnaire_answer = {
                'process_approval_id': approval_id,
                'question_id': question.get('id'),
                'answer': str(question.get('questionnaireAnswer'))
            }

            QuestionnaireRepository.answer_questionnaire(questionnaire_answer)

        QuestionnaireRepository.change_status_to_pending_approval(approval_id)

        return Response.ok_message('successfull')
    else:
        raise Exception('already.answered')


def correct_questionnaire(request):
    data = request.get_json()

    for question_answer in data:
        QuestionnaireRepository.correct_questionnaire(question_answer)

    return {}
