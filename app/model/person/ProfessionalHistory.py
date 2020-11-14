class ProfessionalHistory:
    def __init__(self):
        self.id = 0
        self.id_person = 0
        self.company = None
        self.job = None
        self.description = None
        self.initial_date = None
        self.final_date = None
        self.current_job = False

    def serialize(self):
        return {
            'id': self.id,
            'personId': self.id_person,
            'job': self.job,
            'company': self.company,
            'description': self.description,
            'initialDate': self.initial_date,
            'finalDate': self.final_date,
            'currentJob': self.current_job
        }
