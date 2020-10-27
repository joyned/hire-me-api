class QuestionnaireQuestion:
    def __init__(self):
        self.id = 0
        self.questionnaire_id = 0
        self.question_title = ''
        self.question_help = ''
        self.answer_type = ''
        self.answer_time = None
        self.questionnaire_question_options = []
        self.questionnaire_answer = None
        self.answer_id = None
        self.questionnaire_correct = None

    def serialize(self):
        return {
            'id': self.id,
            'questionnaieId': self.questionnaire_id,
            'questionTitle': self.question_title,
            'questionHelp': self.question_help,
            'answerType': self.answer_type,
            'answerTime': self.answer_time,
            'questionnaireQuestionOption': self.questionnaire_question_options,
            'questionnaireAnswer': self.questionnaire_answer,
            'answerId': self.answer_id,
            'questionnaireCorrect': self.questionnaire_correct
        }
