class JobSelectiveProcess:
    def __init__(self):
        self.id = None
        self.step_title = ''
        self.step_description = ''
        self.step_type = ''
        self.questionnaire_id = None
        self.order = None
        self.status = 'P'

    def serialize(self):
        return {
            'id': self.id,
            'stepTitle': self.step_title,
            'stepDescription': self.step_description,
            'stepType': self.step_type,
            'questionnaireId': self.questionnaire_id,
            'order': self.order,
            'status': self.status
        }