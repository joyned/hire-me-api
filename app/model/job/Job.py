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
        self.job_benefits = []
        self.company = ""
        self.status = ""

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'salary': self.salary,
            'description': self.description,
            'areaId': self.id_area,
            'jobLevelId': self.id_job_level,
            'jobBenefits': self.job_benefits,
            'company': self.company,
            'status': self.status
        }

