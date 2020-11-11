from app.model.email.EmailMessage import EmailMessage
from app.service.email import EmailService


def send_contact_email(request):
    email_message = EmailMessage()
    data = request.get_json()

    email = data.get('email')
    name = data.get('name')
    position = data.get('position')
    message = data.get('message')

    email_body = """
        <h1>Contato</h1>
        <p><b>Pessoa: </b>{0}</p>
        <p><b>Sou: </b>{1}</p>
        <p><b>Email: </b>{2}</p>
        <hr>
        <p>{3}</p>
    """.format(name, position, email, message)

    email_message.to = 'brunodsbg@gmail.com';
    email_message.body = email_body
    email_message.subject = 'Contato'
    email_message.from_email = 'panico400@gmail.com'

    EmailService.send_email(email_message)
