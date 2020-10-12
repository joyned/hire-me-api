from app.model.questionnaire.QuestionnaireQuestion import QuestionnaireQuestion


class Questionnaire:
    def __init__(self):
        self.id = 0
        self.title = ''
        self.status = False
        self.creation_date = ''
        self.company_id = 0
        self.user_id = 0
        self.questionnaire_questions = []

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'status': self.status,
            'creationDate': self.creation_date,
            'companyId': self.company_id,
            'userId': self.user_id,
            'questionnaireQuestions': self.questionnaire_questions
        }
