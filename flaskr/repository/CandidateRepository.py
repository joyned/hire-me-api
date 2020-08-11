from flaskr.database import database as db


def get_candidate_details(candidate_id):
    sql = """
        SELECT  Id,
                Nome,
                CPF,
                RG,
                Nome_Completo,
                Data_Nascimento,
                Cidade,
                Estado,
                Pais,
                Endereco,
                Endereco_Numero,
                CEP,
                Complemento,
                Email
        FROM    Candidato
        WHERE   Id = %d
    """
    return db.execute_query_fetchone(sql, candidate_id)


def update_candidate(candidate):
    sql = """
    UPDATE Candidato
    SET Nome = %s,
        CPF = %d,
        RG = %d,
        Nome_Completo = %s,
        Data_Nascimento = %s,
        Cidade = %s,
        Estado = %s,
        Pais = %s,
        Endereco = %s,
        Endereco_Numero = %s,
        CEP  = %d,
        Complemento = %s,
        Email = %s
    WHERE Id = %d
    """
    params = (
        candidate.name,
        candidate.cpf,
        candidate.rg,
        candidate.full_name,
        candidate.birth_date,
        candidate.city,
        candidate.state,
        candidate.country,
        candidate.address,
        candidate.address_number,
        candidate.cep,
        candidate.complement,
        candidate.email,
        candidate.id
    )

    db.execute_insert(sql, params)