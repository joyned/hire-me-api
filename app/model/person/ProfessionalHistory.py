class ProfessionalHistory:
    def __init__(self):
        self.id = 0
        self.id_person = 0
        self.company = None
        self.job = None
        self.description = None
        self.initialDate = None
        self.finalDate = None
        self.currentJob = False

    def serialize(self):
        return {
            'id': self.id,
            'personId': self.id_person,
            'job': self.job,
            'company': self.company,
            'description': self.description,
            'initialDate': self.initialDate,
            'finalDate': self.finalDate,
            'currentJob': self.currentJob
        }
