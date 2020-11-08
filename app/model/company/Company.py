class Company:
    def __init__(self):
        self.id = 0
        self.name = None

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
