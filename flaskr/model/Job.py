class Job:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.localization = ""

        def serialize(self):
            return {
                'id': self.id,
                'title': self.book_code,
                'localization': self.read_status,
            }