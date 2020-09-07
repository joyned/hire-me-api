from app.model.context.HireMeContext import HireMeContext
from app.model.person.Person import Person
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

    return person.serialize()


def update_candidate_details(request):
    data = request.get_json()
    person = Person()
    person.city = data['city']
    person.state = data['state']
    person.country = data['country']
    person.photo = data['photo']
    return PersonRepository.update_person(person)
