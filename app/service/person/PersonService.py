from app.model.context.HireMeContext import HireMeContext
from app.model.person.Person import Person
from app.model.person.PersonHability import PersonAbility
from app.model.person.ProfessionalHistory import ProfessionalHistory
from app.repository.person import PersonRepository


def get_person_details(request):
    context = HireMeContext()
    context.build(request)

    person = Person()

    result = PersonRepository.get_candidate_details(context.person_id)

    if result is not None:
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
    return {}


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

    for row in PersonRepository.get_professional_histories(context.person_id):
        professional_history = ProfessionalHistory()
        professional_history.id = row[0]
        professional_history.id_person = row[1]
        professional_history.company = row[2]
        professional_history.job = row[3]
        professional_history.description = row[4]
        professional_history.initial_date = row[5]
        professional_history.final_date = row[6]
        professional_history.current_job = row[7] == 'T'

        professional_histories.append(professional_history.serialize())

    return professional_histories


def professional_history(request):
    context = HireMeContext()
    context.build(request)

    data = request.get_json()

    professional_history = ProfessionalHistory()

    professional_history.id = data.get('id')
    professional_history.id_person = data.get('personId')
    professional_history.company = data.get('company')
    professional_history.job = data.get('job')
    professional_history.description = data.get('description')
    professional_history.initial_date = data.get('initialDate')
    professional_history.final_date = data.get('finalDate')
    professional_history.current_job = data.get('currentJob')

    if professional_history.id is not None and professional_history.id > 0:
        PersonRepository.update_professional_history(professional_history)
    else:
        PersonRepository.insert_professional_history(professional_history, context)


def delete_professional_history(professional_history_id):
    PersonRepository.delete_professional_history(professional_history_id)


def get_abilities(request):
    context = HireMeContext()
    context.build(request)

    abilities = []

    for row in PersonRepository.get_abilities(context.person_id):
        abilities.append(row[0])

    return abilities


def insert_ability(request):
    context = HireMeContext()
    context.build(request)

    data = request.get_json()

    delete_abilities(context)

    for row_ability in data:
        PersonRepository.insert_abilities(context, row_ability)


def delete_abilities(context: HireMeContext):
    PersonRepository.delete_abilities(context)


def get_person_profile(person_id):
    person = Person()
    person_professional_histories = []
    person_abilities = []

    person_data = PersonRepository.get_person_profile(person_id)
    person_professional_history_data = PersonRepository.get_professional_histories(person_id)
    person_abilities_data = PersonRepository.get_abilities(person_id)

    if person_data is not None:
        person.id = person_id
        person.photo = person_data[0]
        person.name = person_data[1]
        person.fullname = person_data[2]
        person.city = person_data[3]
        person.state = person_data[4]
        person.birthdate = person_data[5]

    if person_professional_history_data is not None and len(person_professional_history_data) > 0:
        for professional_history_row in person_professional_history_data:
            professional_history = ProfessionalHistory()
            professional_history.id = professional_history_row[0]
            professional_history.id_person = professional_history_row[1]
            professional_history.company = professional_history_row[2]
            professional_history.job = professional_history_row[3]
            professional_history.description = professional_history_row[4]
            professional_history.initial_date = professional_history_row[5]
            professional_history.final_date = professional_history_row[6]
            if professional_history_row[0] == "T":
                professional_history.current_job = "T"
            else:
                professional_history.current_job = "F"
            person_professional_histories.append(professional_history.serialize())

    if person_abilities_data is not None and len(person_abilities_data) > 0:
        for person_abilities_row in person_abilities_data:
            person_ability = PersonAbility()
            person_ability.person_id = person_id
            person_ability.ability = person_abilities_row[0]
            person_abilities.append(person_ability.serialize())

    return {
        'person': person.serialize(),
        'professionalHistories': person_professional_histories,
        'abilities': person_abilities
    }
