from flaskr.database import database as db


def get_candidate_details(person_id):
    sql = """
    SELECT  Pessoa.Id,
            Pessoa.Id_Usuario,
            Pessoa.Nome,
            Pessoa.Nome_Completo,
            Pessoa.CPF,
            Pessoa.RG,
            Pessoa.Cidade,
            Pessoa.Estado,
            Pessoa.Pais,
            Pessoa.Foto,
            Pessoa.Data_Nascimento,
            PessoaEndereco.Endereco,
            PessoaEndereco.Numero,
            PessoaEndereco.Complemento,
            PessoaEndereco.CEP
      FROM  Pessoa
      JOIN  PessoaEndereco
         ON PessoaEndereco.Id_Pessoa = Pessoa.Id
    WHERE Pessoa.Id = %d
    """
    return db.execute_query_fetchone(sql, person_id)


def update_person(person):
    sql = """
    UPDATE  Pessoa 
    SET     Cidade = %s,
            Estado = %s,
            Pais = %s,
            Foto = %s
    """
    param = (person.city, person.state, person.country, person.photo)

    db.execute_insert(sql, param)
