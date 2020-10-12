class QuestionnaireQuestionOption:
    def __init__(self):
        self.id = 0
        self.option_title = ''
        self.questionnaire_question_id = 0

    def serialize(self):
        return {
            'id': self.id,
            'optionTitle': self.option_title,
            'questionnaireQuestionId': self.questionnaire_question_id
        }
