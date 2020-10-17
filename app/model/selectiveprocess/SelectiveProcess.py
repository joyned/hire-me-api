class SelectiveProcess:
    def __init__(self):
        self.id = 0
        self.title = ''
        self.company_id = 0
        self.user_id = 0
        self.status = False
        self.steps = []

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'companyId': self.company_id,
            'userId': self.user_id,
            'status': self.status,
            'steps': self.steps
        }