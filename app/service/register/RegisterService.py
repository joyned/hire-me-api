from werkzeug.security import generate_password_hash

from app.model.email.EmailMessage import EmailMessage
from app.model.person.Person import Person
from app.repository.register import RegisterRepository
from app.service.email import EmailService
from app.service.person import PersonService


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
        insert_person_abilities(person_id, data.get('abilities'))
        PersonService.person_education_batch(request, person_id)
        send_welcome_email(data)


# TODO: Remover o replace da String aqui e colocar no Frontend
def register_new_user(request, hash_password):
    person = Person()

    person.user.email = request.get('user').get('email')
    person.user.password = hash_password
    person.name = request.get('name')
    person.fullname = request.get('fullname')
    person.cpf = request.get('cpf')
    person.rg = request.get('rg')
    person.birthdate = request.get('birthdate')
    person.city = request.get('city')
    person.state = request.get('state')
    person.country = request.get('country')
    person.photo = request.get('photo')
    person.person_addres.address = request.get('personAddress').get('address')
    person.person_addres.number = request.get('personAddress').get('number')
    person.person_addres.cep = request.get('personAddress').get('cep').replace('-', '')
    person.person_addres.complement = request.get('personAddress').get('complement')

    return RegisterRepository.register_new_user(person)


def insert_person_professional_history(person_id, data):
    if data is not None:
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


def insert_person_abilities(person_id, data):
    if data is not None:
        for row in data:
            person_ability = (
                person_id,
                row
            )

            RegisterRepository.insert_person_ability(person_ability)


def check_if_email_exists(email):
    result = RegisterRepository.check_if_email_exists(email)
    if result is not None:
        return 'user_already_exists'
    else:
        return 'user_avaliable'


def register_error_message(error):
    if error == "user_already_exists":
        return 'user.already.exists'


def send_welcome_email(request):
    email_message = EmailMessage()

    email_message.to = request.get('user').get('email')
    email_message.subject = 'HireMe - Bem-vindo!'
    email_message.from_email = 'hiremecop@gmail.com'
    email_message.body = """
        <h1>Bem vindo!!!</h1>
		<p>Estamos super contentes de ter você conosco.</p>
		<p>Queriamos te dar as boas-vindas ao HireMe, esperamos que você consiga encontrar sua vaga ideal.</p>
		<br>
		<p><b>Atenciosamente,</b></p>
		<p><b>Equipe HireMe</b></p>
    """

    EmailService.send_email(email_message)
