from app.database import Database as db


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
            PessoaEndereco.CEP,
            Usuario.Email
      FROM  Pessoa
      JOIN  PessoaEndereco
         ON PessoaEndereco.Id_Pessoa = Pessoa.Id
      JOIN  Usuario
         ON Usuario.Id = Pessoa.Id_Usuario
    WHERE Pessoa.Id = ?
    """
    return db.execute_query_fetchone(sql, person_id)


def update_person(person):
    sql = """
    UPDATE  Pessoa 
    SET     Cidade = ?,
            Estado = ?,
            Pais = ?,
            Foto = ?
    WHERE   Id = ?
    """
    param = (person.city, person.state, person.country, person.photo, person.id)

    db.execute_insert(sql, param)
