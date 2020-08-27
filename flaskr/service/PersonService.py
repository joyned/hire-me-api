from flask import Blueprint, jsonify
from flask import request
from flask_cors import cross_origin

from flaskr.model.Person import Person
from flaskr.repository import PersonRepository
from flaskr.model.HireMeContext import HireMeContext
from flaskr.response import Response
from flaskr.security.TokenValidator import token_validator

person_service = Blueprint('person_service', __name__)


@token_validator(request)
@person_service.route('/api/person/get', methods=['GET'])
@cross_origin()
def get_candidate_details():
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

    return Response.ok(person.serialize())


@token_validator(request)
@person_service.route('/api/person/update', methods=['POST'])
@cross_origin()
def update_candidate_details():
    data = request.get_json()
    person = Person()
    person.city = data['city']
    person.state = data['state']
    person.country = data['country']
    person.photo = data['photo']
    try:
        return Response.ok(PersonRepository.update_person(person))
    except Exception as e:
        return Response.error(e)
