from werkzeug.security import generate_password_hash

from app.repository.register import RegisterRepository


def register(request):
    data = request.get_json()
    email = data.get('user').get('email')
    hash_password = generate_password_hash(data.get('user').get('password'), method='sha256')
    check_user = check_if_email_exists(email)
    if not check_user == "user_avaliable":
        raise Exception(register_error_message(check_user))
    else:
        person_id = register_new_user(data, hash_password)
        insert_person_professional_history(person_id, data.get('professionalHistory'))


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
    return RegisterRepository.register_new_user(user)


def insert_person_professional_history(person_id, data):
    for row in data:
        if row.get('currentJob'):
            current_job = 'T'
        else:
            current_job = 'F'

        professional_history = (
            person_id,
            row.get('company'),
            row.get('job'),
            row.get('description'),
            row.get('initialDate'),
            row.get('finalDate'),
            current_job
        )

        RegisterRepository.insert_person_professional_history(professional_history)


def check_if_email_exists(email):
    result = RegisterRepository.check_if_email_exists(email)
    if result is not None:
        return 'user_already_exists'
    else:
        return 'user_avaliable'


def register_error_message(error):
    if error == "user_already_exists":
        return 'user.already.exists'
