class ResponseModel:
    def __init__(self):
        self.ok = True
        self.payload = None

    def serialize(self):
        return {
            'ok': self.ok,
            'payload': self.payload
        }
