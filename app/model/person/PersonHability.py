class PersonAbility:
    def __init__(self):
        self.id = None
        self.person_id = None
        self.ability = None

    def serialize(self):
        return {
            'id': self.id,
            'personId': self.person_id,
            'ability': self.ability
        }