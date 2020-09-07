class User:
    def __init__(self):
        self.id = 0
        self.email = ""
        self.password = ""
        self.user_profile_id = 0

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'user_profile_id': self.user_profile_id
        }