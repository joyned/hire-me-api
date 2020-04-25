class Pages:
    def __init__(self):
        self.id = 0
        self.constant = ''
        self.name = '',
        self.active = False

    def serialize(self):
        return {
            "id": self.id,
            "constant": self.constant,
            "name": self.name,
            "active": self.active
        }