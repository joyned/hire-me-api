class Messages:
    def __init__(self):
        self.id = None
        self.from_id = None
        self.from_name = None
        self.to_id = None
        self.to_name = None
        self.message = None
        self.sent_date = None
        self.mine = None
        self.room_id = None

    def serialize(self):
        return {
            'id': self.id,
            'fromId': self.from_id,
            'fromName': self.from_name,
            'toId': self.to_id,
            'toName': self.to_name,
            'message': self.message,
            'sentDate': self.sent_date,
            'mine': self.mine,
            'roomId': self.room_id
        }