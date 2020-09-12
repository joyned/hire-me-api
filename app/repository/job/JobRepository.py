from app.database import database as db


def get_jobs():
    sql = """
        SELECT Id,
               Nome,
               Cidade,
               Estado,
               Pais,
               Descricao
        FROM   Vaga
    """
    return db.execute_query_fetchall(sql, None)


def filter_jobs(job_filter):
    params = []
    sql = """
            SELECT Id,
                   Nome,
                   Cidade,
                   Estado,
                   Pais,
                   Descricao
            FROM   Vaga
            WHERE 1 = 1
        """

    if job_filter.job is not None:
        sql += " AND Nome LIKE %s"
        params.append(job_filter.job + "%")

    if job_filter.localization is not None:
        sql += """
            AND (
                Cidade LIKE %s
                OR Estado LIKE %s
                OR Pais LIKE %s
            )
        """
        params.append(job_filter.localization + "%")
        params.append(job_filter.localization + "%")
        params.append(job_filter.localization + "%")

    return db.execute_query_fetchall(sql, tuple(params))


def get_job_by_id(id):
    sql = """
        SELECT Id,
               Nome,
               Cidade,
               Estado,
               Pais,
               Salario,
               Descricao
        FROM   Vaga
        WHERE  Id = %d
    """
    param = (id)
    return db.execute_query_fetchone(sql, param)


def get_job_benefits(job_id):
    sql = """
        SELECT Id_Vaga,
               Beneficio
        FROM VagaBeneficios
        WHERE Id_Vaga = %d
    """

    return db.execute_query_fetchall(sql, (job_id))


def apply_to_job(person_id, job_id):
    sql = """
        insert into VagasAplicadas (Id_Vaga, Id_Pessoa) values (%d, %d)
    """
    param = (job_id, person_id)
    db.execute_insert(sql, param)


def check_if_person_are_applied_to_job(person_id, job_id):
    sql = """
        SELECT 1 FROM VagasAplicadas WHERE Id_Vaga = %d AND Id_Pessoa = %d
    """

    param = (job_id, person_id)
    return db.execute_query_fetchone(sql, param)


def get_applied_jobs(person_id):
    sql = """
    SELECT  Vaga.Id,
            Vaga.Nome,
            Vaga.Cidade,
            Vaga.Estado,
            Vaga.Pais
    FROM    Vaga
    JOIN VagasAplicadas
    ON VagasAplicadas.Id_Vaga = Vaga.Id
    AND VagasAplicadas.Id_Pessoa = %d
    """
    param = (person_id)
    return db.execute_query_fetchall(sql, param)


# TODO: THIS METHOD NEEDS TO BE REVIEWED, IS NOT GOOD DELETE SOMETHING FROM DATABASE, NEED TO CONSIDER CREATE A FLAG
#  TO SET INACTIVE
def delete_apply_to_job(person_id, job_id):
    sql = """
            delete from VagasAplicadas where Id_Vaga = %d and Id_Pessoa = %d
        """
    param = (job_id, person_id)
    db.execute_delete(sql, param)
