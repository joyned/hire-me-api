class Job:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.city = ""
        self.state = ""
        self.country = ""
        self.salary = ""
        self.description = ""
        self.job_benefits = []
        self.company = ""
        self.status = ""
        self.user_id = ""
        self.selective_process_id = None

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'salary': self.salary,
            'description': self.description,
            'jobBenefits': self.job_benefits,
            'company': self.company,
            'status': self.status,
            'userId': self.user_id,
            'selectiveProcessId': self.selective_process_id
        }

