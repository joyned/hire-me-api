class QuestionnaireQuestionAnswer:
    def __init__(self):
        self.id = 0
        self.questionnaire_question_id = 0
        self.answer_option_id = 0
        self.answer_text = ''

    def serialize(self):
        return {
            'id': self.id,
            'questionnaireQuestionId': self.questionnaire_question_id,
            'answerOptionId': self.answer_option_id,
            'answerText': self.answer_text
        }
