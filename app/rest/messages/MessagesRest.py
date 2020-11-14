from flask import Blueprint, request

from app.security.TokenValidator import token_validator
from app.service.message import MessagesService
from app.utils.response import Response

messages_rest = Blueprint('messages_rest', __name__)


@messages_rest.route('/api/messages/get/<to_id>', methods=['GET'])
@token_validator(request)
def get_messages(to_id):
    return Response.execute(MessagesService.get_messages, request, to_id, error_status_code=400)


@messages_rest.route('/api/messages/send', methods=['POST'])
@token_validator(request)
def send_message():
    return Response.execute(MessagesService.send_message, request, error_status_code=400)


@messages_rest.route('/api/message/candidate/list', methods=['GET'])
@token_validator(request)
def list_candidate_messages():
    return Response.execute(MessagesService.list_candidate_messages, request, error_status_code=400)


@messages_rest.route('/api/message/candidate/<room_id>', methods=['GET'])
@token_validator(request)
def get_candidate_messages_by_room_id(room_id):
    return Response.execute(MessagesService.get_candidate_messages_by_room_id, request, room_id, error_status_code=400)


@messages_rest.route('/api/message/candidate/send', methods=['POST'])
@token_validator(request)
def send_message_to_room():
    return Response.execute(MessagesService.send_message_to_room, request, error_status_code=400)