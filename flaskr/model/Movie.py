class Movie:
    def __init__(self):
        self.page_id = 2
        self.id = 0
        self.name = ''
        self.description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    def serialize(self):
        return {
            'page_id': self.page_id,
            'id': self.id,
            'name': self.name,
            'description': self.description
        }