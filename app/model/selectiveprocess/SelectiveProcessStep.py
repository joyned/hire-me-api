class SelectiveProcessStep:
    def __init__(self):
        self.id = 0
        self.step_title = ''
        self.step_description = ''
        self.step_type = ''
        self.questionnaire_id = None
        self.selective_process_id = 0

    def serialize(self):
        return {
            'id': self.id,
            'stepTitle': self.step_title,
            'stepDescription': self.step_description,
            'stepType': self.step_type,
            'questionnaireId': self.questionnaire_id
        }
