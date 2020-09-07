from flask import jsonify
from werkzeug.security import generate_password_hash

from app.repository.register import RegisterRepository


def register(request):
    data = request.get_json()
    email = data.get('user').get('email')
    hash_password = generate_password_hash(data.get('user').get('password'), method='sha256')
    check_user = check_if_email_exists(email)
    if not check_user == "user_avaliable":
        return register_error_message(check_user)
    else:
        register_new_user(data, hash_password)
        return 'New user created.'


# TODO: Remover o replace da String aqui e colocar no Frontend
def register_new_user(request, hash_password):
    user = (
        request.get('user').get('email'),
        hash_password,
        request.get('name'),
        request.get('fullname'),
        request.get('cpf'),
        request.get('rg'),
        request.get('birthdate'),
        request.get('city'),
        request.get('state'),
        request.get('country'),
        request.get('photo'),
        request.get('personAddress').get('address'),
        request.get('personAddress').get('number'),
        str(request.get('personAddress').get('cep')).replace('-', ''),
        request.get('personAddress').get('complement')
    )
    RegisterRepository.register_new_user(user)


def check_if_email_exists(email):
    result = RegisterRepository.check_if_email_exists(email)
    if result is not None:
        return 'user_already_exists'
    else:
        return 'user_avaliable'


def register_error_message(error):
    if error == "user_already_exists":
        return 'This user already exists in our system. Please, choose another.'
