from flask import Blueprint, request

from app.service.contact import ContactService
from app.utils.response import Response

contact_rest = Blueprint('contact_rest', __name__)


@contact_rest.route('/api/contact', methods=['POST'])
def send_contact_email():
    return Response.execute(ContactService.send_contact_email, request, error_status_code=404)
