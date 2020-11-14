from app.database import Database as db
from app.model.context.HireMeContext import HireMeContext
from app.model.person.PersonEducation import PersonEducation
from app.model.person.ProfessionalHistory import ProfessionalHistory
from app.utils.logger import Logger


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

    Logger.debug(sql.replace("?", str(person_id)))

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


def get_professional_histories(person_id: int):
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

    param = (person_id,)

    return db.execute_query_fetchall(sql, param)


def insert_professional_history(professional_history: ProfessionalHistory, context: HireMeContext):
    sql = """
        INSERT INTO PessoaHistoricoProfissional (Id_Pessoa, Empresa, Cargo, Descricao, Data_Entrada, Data_Saida, Trabalha_Atualmente)
            VALUES (?,?,?,?,?,?,?)
    """

    if professional_history.current_job:
        current_job = 'T'
    else:
        current_job = 'F'

    param = (
        context.person_id, professional_history.company, professional_history.job, professional_history.description,
        professional_history.initial_date, professional_history.final_date, current_job)

    db.execute_insert(sql, param)


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

    if professional_history.current_job:
        current_job = 'T'
    else:
        current_job = 'F'

    param = (professional_history.company, professional_history.job, professional_history.description,
             professional_history.initial_date, professional_history.final_date, current_job,
             professional_history.id)

    return db.execute_update(sql, param)


def delete_professional_history(professional_history_id):
    sql = """
        DELETE FROM PessoaHistoricoProfissional WHERE Id = ?
    """

    param = (professional_history_id,)

    db.execute_delete(sql, param)


def get_abilities(person_id: int):
    sql = """
        SELECT  Habilidade
        FROM PessoaHabilidades
        WHERE Id_Pessoa = ?
    """

    param = (person_id,)

    return db.execute_query_fetchall(sql, param)


def insert_abilities(context: HireMeContext, ability: str):
    sql = """
        INSERT INTO PessoaHabilidades (Id_Pessoa, Habilidade)
            VALUES (?, ?)
    """

    param = (context.person_id, ability)

    db.execute_insert(sql, param)


def delete_abilities(context: HireMeContext):
    sql = """
        DELETE FROM PessoaHabilidades WHERE Id_Pessoa = ?
    """

    param = (context.person_id,)

    db.execute_delete(sql, param)


def get_person_profile(person_id):
    sql = """
        SELECT  Pessoa.Foto,
                Pessoa.Nome,
                Pessoa.Nome_Completo,
                Pessoa.Cidade,
                Pessoa.Estado,
                Pessoa.Data_Nascimento
        FROM    Pessoa
        WHERE Pessoa.Id = ?
    """

    param = (person_id,)

    return db.execute_query_fetchone(sql, param)


def get_person_education(person_id):
    sql = """
        SELECT  Id,
                Id_Pessoa,
                Instituicao,
                Curso,
                Data_Inicio,
                Data_Fim,
                Cursando
        FROM    PessoaEscolaridade
        WHERE   PessoaEscolaridade.Id_Pessoa = ?
    """

    param = (person_id,)

    return db.execute_query_fetchall(sql, param)

def insert_person_education(person_education: PersonEducation):
    sql = """
        INSERT INTO PessoaEscolaridade (Id_Pessoa, Instituicao, Curso, Data_Inicio, Data_Fim, Cursando)
            VALUES(?,?,?,?,?,?)
    """

    if person_education.current_study:
        current_study = 'T'
    else:
        current_study = 'F'

    param = (
        person_education.person_id, person_education.institution, person_education.course,
        person_education.initial_date,
        person_education.final_date, current_study)

    db.execute_insert(sql, param)


def update_person_education(person_education: PersonEducation):
    sql = """
        UPDATE PessoaEscolaridade
            SET Instituicao = ?,
                Curso = ?,
                Data_Inicio = ?,
                Data_FIm = ?,
                Cursando = ?
            WHERE Id = ?
    """

    if person_education.current_study:
        current_study = 'T'
    else:
        current_study = 'F'

    param = (person_education.institution, person_education.course,
             person_education.initial_date, person_education.final_date, current_study, person_education.id)

    db.execute_update(sql, param)


def delete_person_education(person_education_id):
    sql = """
        DELETE FROM PessoaEscolaridade WHERE Id = ?
    """

    param = (person_education_id,)

    db.execute_delete(sql, param)
