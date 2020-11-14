import uuid

from app.model.context.HireMeContext import HireMeContext
from app.model.messages.Messages import Messages
from app.repository.messages import MessagesRepository


def get_messages(request, to_id):
    context = HireMeContext()
    context.build(request)

    messages = []

    result = MessagesRepository.get_messages(context.person_id, to_id)

    if result is not None:
        for row in result:
            message = Messages()
            message.id = row[0]
            message.from_id = row[1]
            message.from_name = row[2]
            message.to_id = row[3]
            message.to_name = row[4]
            message.message = row[5]
            message.sent_date = row[6]
            message.room_id = row[7]
            if message.from_id == context.person_id:
                message.mine = True
            else:
                message.mine = False
            messages.append(message.serialize())
    room_id = MessagesRepository.get_room_id(context.person_id, to_id)[0]
    return {
        'messages': messages,
        'roomId': room_id[0]
    }


def send_message(request):
    messages = Messages()
    context = HireMeContext()
    context.build(request)

    data = request.get_json()

    messages.room_id = data.get('roomId')
    messages.from_id = context.person_id
    messages.to_id = data.get('toId')
    messages.message = data.get('message')

    if messages.room_id is None or messages.room_id == 0:
        messages.room_id = uuid.uuid1()

    MessagesRepository.insert_new_message(messages)


def list_candidate_messages(request):
    context = HireMeContext()
    context.build(request)

    messages = []

    result = MessagesRepository.list_candidate_messages(context.person_id)

    if result is not None:
        for row in result:
            message = Messages()
            message.from_name = row[0]
            message.room_id = row[1]

            messages.append(message.serialize())

    return messages


def get_candidate_messages_by_room_id(request, room_id):
    context = HireMeContext()
    context.build(request)

    messages = []

    result = MessagesRepository.get_candidate_messages_by_room_id(room_id)

    if result is not None:
        for row in result:
            message = Messages()
            message.id = row[0]
            message.from_id = row[1]
            message.from_name = row[2]
            message.to_id = row[3]
            message.to_name = row[4]
            message.message = row[5]
            message.sent_date = row[6]
            message.room_id = row[7]
            if message.from_id == context.person_id:
                message.mine = True
            else:
                message.mine = False
            messages.append(message.serialize())
    return messages


def send_message_to_room(request):
    messages = Messages()
    context = HireMeContext()
    context.build(request)

    data = request.get_json()

    to_id = MessagesRepository.get_person_id_by_room_id(data.get('roomId'), context)

    messages.room_id = data.get('roomId')
    messages.from_id = context.person_id
    messages.to_id = to_id[0]
    messages.message = data.get('message')

    MessagesRepository.insert_new_message(messages)