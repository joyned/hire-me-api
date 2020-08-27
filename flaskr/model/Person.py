from flaskr.model.PersonAddress import PersonAddress
from flaskr.model.User import User


class Person:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.fullname = ''
        self.cpf = 0
        self.rg = 0
        self.birthdate = ''
        self.city = ''
        self.state = ''
        self.country = ''
        self.photo = ''
        self.person_addres = PersonAddress()
        self.user = User()

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user.id,
            'name': self.name,
            'fullname': self.fullname,
            'cpf': self.cpf,
            'rg': self.rg,
            'birthdate': self.birthdate,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'photo': self.photo,
            'person_addres': self.person_addres.serialize(),
            'user': self.user.serialize()
        }
