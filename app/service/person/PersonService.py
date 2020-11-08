from app.model.context.HireMeContext import HireMeContext
from app.model.person.Person import Person
from app.model.person.ProfessionalHistory import ProfessionalHistory
from app.repository.person import PersonRepository


def get_person_details(request):
    context = HireMeContext()
    context.build(request)

    person = Person()

    result = PersonRepository.get_candidate_details(context.person_id)

    person.id = result[0]
    person.user.id = result[1]
    person.name = result[2]
    person.fullname = result[3]
    person.cpf = result[4]
    person.rg = result[5]
    person.city = result[6]
    person.state = result[7]
    person.country = result[8]
    person.photo = result[9]
    person.birthdate = result[10]
    person.person_addres.address = result[11]
    person.person_addres.number = int(result[12])
    person.person_addres.complement = result[13]
    person.person_addres.cep = int(result[14])
    person.user.email = result[15]
    return person.serialize()


def update_candidate_details(request):
    context = HireMeContext()
    context.build(request)

    data = request.get_json()
    person = Person()
    person.id = context.person_id
    person.city = data['city']
    person.state = data['state']
    person.country = data['country']
    person.photo = data['photo']
    return PersonRepository.update_person(person)


def get_professional_histories(request):
    context = HireMeContext()
    context.build(request)

    professional_histories = []

    for row in PersonRepository.get_professional_histories(context):
        professional_history = ProfessionalHistory()
        professional_history.id = row[0]
        professional_history.id_person = row[1]
        professional_history.company = row[2]
        professional_history.job = row[3]
        professional_history.description = row[4]
        professional_history.initialDate = row[5]
        professional_history.finalDate = row[6]
        professional_history.currentJob = row[7] == 'T'

        professional_histories.append(professional_history.serialize())

    return professional_histories


def update_professional_history(request):
    data = request.get_json()

    professional_history = ProfessionalHistory()

    professional_history.id = data.get('id')
    professional_history.id_person = data.get('personId')
    professional_history.company = data.get('company')
    professional_history.job = data.get('job')
    professional_history.description = data.get('description')
    professional_history.initialDate = data.get('initialDate')
    professional_history.finalDate = data.get('finalDate')
    professional_history.currentJob = data.get('currentJob')

    PersonRepository.update_professional_history(professional_history)
