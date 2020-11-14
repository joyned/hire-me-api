class PersonEducation:
    def __init__(self):
        self.id = None
        self.person_id = None
        self.institution = None
        self.course = None
        self.initial_date = None
        self.final_date = None
        self.current_study = None

    def serialize(self):
        return {
            'id': self.id,
            'personId': self.person_id,
            'institution': self.institution,
            'course': self.course,
            'initialDate': self.initial_date,
            'finalDate': self.final_date,
            'currentStudy': self.current_study
        }
