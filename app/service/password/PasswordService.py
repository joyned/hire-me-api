from app.model.context.HireMeContext import HireMeContext
from app.model.email.EmailMessage import EmailMessage
from app.repository.password import PasswordRepository
from app.service.email import EmailService
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

import random
import string


def reset_password(request):
    data = request.get_json()
    email = data.get('email')

    if PasswordRepository.check_if_email_exists(email) is not None:
        email_message = EmailMessage()
        new_password = generate_random_password()

        email_message.body = """
                <h1>Senha</h1>
                <p>Sua nova senha é: <b>{0}</b></p>
            """.format(new_password)

        email_message.from_email = 'hiremecop@gmail.com'
        email_message.to = email
        email_message.subject = 'Hire Me - Nova senha'

        hash_password = generate_password_hash(new_password, method='sha256')

        PasswordRepository.update_password_by_email(email, hash_password)

        return EmailService.send_email(email_message)
    else:
        return 'email.not.found'


def generate_random_password():
    sample_str = ''.join((random.choice(string.ascii_letters) for i in range(5)))
    sample_str += ''.join((random.choice(string.digits) for i in range(5)))
    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string


def change_password(request):
    context = HireMeContext()
    context.build(request)

    data = request.get_json()

    hash_pwd = PasswordRepository.get_hash_password_by_user_id(context)[0]

    if check_password_hash(hash_pwd, data.get('currentPassword')):
        new_hash_password = generate_password_hash(data.get('newPassword'), method='sha256')
        PasswordRepository.update_password_by_user_id(context, new_hash_password)
    else:
        raise AssertionError('wrong.password')
