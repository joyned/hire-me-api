class Candidate:
    def __init__(self):
        self.user_id = 0
        self.id = 0
        self.name = ''
        self.cpf = 0
        self.rg = 0
        self.full_name = ''
        self.birth_date = ''
        self.city = ''
        self.state = ''
        self.country = ''
        self.address = ''
        self.address_number = 0
        self.cep = 0
        self.complement = ''
        self.email = ''

    def serialize(self):
        return {
            'user_id': self.user_id,
            'id': self.id,
            'name': self.name,
            'cpf': self.cpf,
            'rg': self.rg,
            'full_name': self.full_name,
            'birth_date': self.birth_date,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'address': self.address,
            'address_number': self.address_number,
            'cep': self.cep,
            'complement': self.complement,
            'email': self.email
        }
