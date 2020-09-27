class JobChart:
    def __init__(self):
        self.total = 0
        self.date = ''
        self.company_id = 0

    def serialize(self):
        return {
            'total': self.total,
            'date': self.date,
            'companyId': self.company_id
        }