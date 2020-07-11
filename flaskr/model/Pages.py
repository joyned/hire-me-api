class Pages:
    def __init__(self):
        self.id = 0
        self.constant = ''
        self.name = ''
        self.icon = ''

    def serialize(self):
        return {
            "id": self.id,
            "constant": self.constant,
            "name": self.name,
            "icon": self.icon
        }