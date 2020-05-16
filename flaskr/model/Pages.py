class Pages:
    def __init__(self):
        self.id = 0
        self.constant = ''
        self.name = ''

    def serialize(self):
        return {
            "id": self.id,
            "constant": self.constant,
            "name": self.name
        }