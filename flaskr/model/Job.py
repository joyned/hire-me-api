class Job:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.city = ""
        self.state = ""
        self.country = ""
        self.salary = ""
        self.description = ""
        self.id_area = 0
        self.id_job_level = 0

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'salary': self.salary,
            'description': self.description,
            'id_area': self.id_area,
            'id_job_level': self.id_job_level
        }

