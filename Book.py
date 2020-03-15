class Book:
    def __init__(self):
        self.page_id = 1
        self.id = 0
        self.book_code = 0
        self.read_status = ''
        self.name = ''
        self.price = 0
        self.description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    def serialize(self):
        return {
            'page_id': self.page_id,
            'id': self.id,
            'book_code': self.book_code,
            'read_status': self.read_status,
            'name': self.name,
            'price': self.price,
            'description': self.description
        }