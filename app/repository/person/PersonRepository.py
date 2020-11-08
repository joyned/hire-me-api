from app.database import Database as db
from app.model.context.HireMeContext import HireMeContext
from app.model.person.ProfessionalHistory import ProfessionalHistory


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


def get_professional_histories(context: HireMeContext):
    sql = """
        SELECT  Id,
                Id_Pessoa,
                Empresa,
                Cargo,
                Descricao,
                Data_Entrada,
                Data_Saida,
                Trabalha_Atualmente
        FROM    PessoaHistoricoProfissional
        WHERE Id_Pessoa = ?
        ORDER BY Data_Entrada DESC
    """

    param = (context.person_id,)

    return db.execute_query_fetchall(sql, param)


def update_professional_history(professional_history: ProfessionalHistory):
    sql = """
        UPDATE PessoaHistoricoProfissional
            SET Empresa = ?,
                Cargo = ?,
                Descricao = ?,
                Data_Entrada = ?,
                Data_Saida = ?,
                Trabalha_Atualmente = ?
        WHERE Id = ?
    """

    if professional_history.currentJob:
        current_job = 'T'
    else:
        current_job = 'F'

    param = (professional_history.company, professional_history.job, professional_history.description,
             professional_history.initialDate, professional_history.finalDate, current_job,
             professional_history.id)

    return db.execute_update(sql, param)
