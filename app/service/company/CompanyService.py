from app.model.company.Company import Company
from app.repository.company import CompanyRepository


def get_companies():
    companies = []
    result = CompanyRepository.get_companies()
    for row in result:
        company = Company()
        company.id = row[0]
        company.name = row[1]
        companies.append(company.serialize())

    return companies


def company(request):
    data = request.get_json()
    company_id = data.get('id')
    company_name = data.get('name')

    if company_id is None:
        create_company(company_name)
    else:
        update_company(company_id, company_name)


def create_company(company_name):
    CompanyRepository.create_company(company_name)


def update_company(company_id, company_name):
    CompanyRepository.update_company(company_id, company_name)


def delete_company(company_id):
    if len(CompanyRepository.check_if_is_deletable(company_id)) == 0:
        CompanyRepository.delete_company(company_id)
    else:
        raise Exception('not.deletable')
