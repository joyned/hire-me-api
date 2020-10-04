from app.database import database as db


def save_new_job(job):
    sql = """
        INSERT INTO Vaga (Nome, Cidade, Estado, Salario, Descricao, Id_Empresa, Id_Usuario, Status)
            VALUES (%s, %s, %s, %d, %s, %d, %d, %s)
    """

    param = (job.title, job.city, job.state, job.salary, job.description, job.company, job.user_id, 'T')

    return db.execute_insert(sql, param)


def save_job_benefits(job):
    for benefit in job.job_benefits:
        sql = """
            INSERT INTO VagaBeneficios (Id_Vaga, Beneficio)
                VALUES (%d, %s)
        """

        param = (job.id, benefit.benefit)

        db.execute_insert(sql, param)


def update_job(job):
    sql = """
     UPDATE Vaga SET
        Nome = %s,
        Cidade = %s,
        Estado = %s,
        Salario = %d,
        Descricao = %s
    WHERE Id = %d
    """

    param = (job.title, job.city, job.state, job.salary, job.description, job.id)
    db.execute_insert(sql, param)


def delete_job_benefits(job_id):
    sql = """
        DELETE FROM VagaBeneficios WHERE Id_Vaga = %d
    """

    param = (job_id)

    db.execute_delete(sql, param)


def get_jobs():
    sql = """
        SELECT  Vaga.Id,
                Vaga.Nome,
                Vaga.Cidade,
                Vaga.Estado,
                Vaga.Pais,
                Vaga.Descricao,
                Empresa.Nome
        FROM    Vaga
        JOIN Empresa
        ON Empresa.Id = Vaga.Id_Empresa
        WHERE Vaga.Status = 'T'
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
            WHERE Vaga.Status = 'T'
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
        SELECT  Vaga.Id,
                Vaga.Nome,
                Vaga.Cidade,
                Vaga.Estado,
                Vaga.Pais,
                Vaga.Salario,
                Vaga.Descricao,
                Empresa.Nome
        FROM    Vaga
        JOIN Empresa
        ON Empresa.Id = Vaga.Id_Empresa
        WHERE Vaga.Id = %d
        AND Vaga.Status = 'T'
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
    WHERE Vaga.Status = 'T'
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


def get_jobs_by_user_id(user_id):
    sql = """
        SELECT  Id,
                Nome,
                Status
        FROM Vaga 
        WHERE Id_Usuario = %d
    """

    param = (user_id)
    return db.execute_query_fetchall(sql, param)


def get_data_to_chart_from_x_days(days, company_id):
    sql = """
    SELECT COUNT(*),
           VagasAplicadas.Data_Aplicacao,
           Vaga.Id_Empresa
    FROM VagasAplicadas
    JOIN Vaga
    ON Vaga.Id = VagasAplicadas.Id_Vaga
    WHERE Data_Aplicacao BETWEEN (GETDATE() - %d) AND (GETDATE())
    AND Vaga.Id_Empresa = %d
    GROUP BY VagasAplicadas.Data_Aplicacao,
             Vaga.Id_Empresa
    """

    param = (days, company_id)

    return db.execute_query_fetchall(sql, param)


def get_candidates_by_job_id(job_id):
    sql = """
        SELECT  Pessoa.Nome,
                VagasAplicadas.Data_Aplicacao
        FROM    VagasAplicadas
        JOIN Pessoa
        ON Pessoa.Id = VagasAplicadas.Id_Pessoa
        WHERE VagasAplicadas.Id_Vaga = %d
    """

    param = (job_id)

    return db.execute_query_fetchall(sql, param)


def change_job_status(status, job_id):
    sql = """
        UPDATE Vaga
            SET Status = %s
        WHERE Id = %d
    """

    param = (status, job_id)
    db.execute_insert(sql, param)
