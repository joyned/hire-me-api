from flask import Blueprint
from flask import jsonify, request
from flask_cors import cross_origin

import flaskr.repository.CandidateRepository as CandidateRepository
from flaskr.model.Candidate import Candidate
from flaskr.model.HireMeContext import HireMeContext
from flaskr.security.TokenValidator import token_validator

candidate_service = Blueprint('candidate_service', __name__)


@token_validator(request)
@candidate_service.route('/api/candidate/get', methods=['GET'])
@cross_origin()
def get_candidate_details():
    context = HireMeContext()
    context.build(request)
    result = CandidateRepository.get_candidate_details(context.candidate_id)
    candidate = Candidate()
    candidate.id = result[0]
    candidate.name = result[1]
    candidate.cpf = result[2]
    candidate.rg = result[3]
    candidate.full_name = result[4]
    candidate.birth_date = result[5]
    candidate.city = result[6]
    candidate.state = result[7]
    candidate.country = result[8]
    candidate.address = result[9]
    candidate.address_number = result[10]
    candidate.cep = result[11]
    candidate.complement = result[12]
    candidate.email = result[13]

    return jsonify(candidate.serialize())


@token_validator(request)
@candidate_service.route('/api/candidate/update', methods=['POST'])
@cross_origin()
def update_candidate_details():
    data = request.get_json()
    candidate = Candidate()
    candidate.id = data['id']
    candidate.name = data['name']
    candidate.cpf = data['cpf']
    candidate.rg = data['rg']
    candidate.full_name = data['full_name']
    candidate.birth_date = data['birth_date']
    candidate.city = data['city']
    candidate.state = data['state']
    candidate.address = data['address']
    candidate.address_number = data['address_number']
    candidate.cep = data['cep']
    candidate.complement = data['complement']
    candidate.email = data['email']
    try:
        CandidateRepository.update_candidate(candidate)
        return jsonify({'ok': True})
    except Exception as e:
        return jsonify({'ok': False, 'error': e})
