from flask import Blueprint, request

from app.security.TokenValidator import token_validator
from app.service.company import CompanyService
from app.utils.response import Response

company_rest = Blueprint('company_rest', __name__)


@company_rest.route('/api/company/get', methods=['GET'])
@token_validator(request)
def get_companies():
    return Response.execute(CompanyService.get_companies, error_status_code=403)


@company_rest.route('/api/company', methods=['PUT'])
@token_validator(request)
def company():
    return Response.execute(CompanyService.company, request, error_status_code=403)


@company_rest.route('/api/company/delete/<company_id>', methods=['DELETE'])
@token_validator(request)
def delete_company(company_id):
    return Response.execute(CompanyService.delete_company, company_id, error_status_code=403)
