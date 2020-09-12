class PersonAddress:
    def __init__(self):
        self.id = 0
        self.person_id = 0
        self.address = ''
        self.number = ''
        self.cep = 0
        self.complement = ''

    def serialize(self):
        return {
            'id': self.id,
            'personId': self.id,
            'address': self.address,
            'number': self.number,
            'cep': self.cep,
            'complement': self.complement
        }
