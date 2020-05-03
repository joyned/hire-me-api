from flaskr.database import database as db


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


def get_job_by_id(id):
    sql = """
        SELECT Id,
               Nome,
               Cidade,
               Estado,
               Pais,
               Salario,
               Descricao,
               Cod_Area,
               Cod_Nivel_Cargo
        FROM   Vaga
        WHERE  Id = %d
    """
    param = (id)
    return db.execute_query_fetchone(sql, param)


def apply_to_job(userId, jobId):
    sql = """
        insert into VagasAplicadas (Id_Vaga, Id_Candidato) values (%d, %d)
    """
    param = (jobId, userId)
    db.execute_insert(sql, param)


def get_applied_jobs(userId):
    sql = """
    SELECT  Vaga.Id,
            Vaga.Nome,
            Vaga.Cidade,
            Vaga.Estado,
            Vaga.Pais
    FROM    Vaga
    JOIN VagasAplicadas
    ON VagasAplicadas.Id_Vaga = Vaga.Id
    AND VagasAplicadas.Ativo = 'T'
    AND VagasAplicadas.Id_Candidato = %d
    """
    param = (userId)
    return db.execute_query_fetchall(sql, param)


# TODO: THIS METHOD NEEDS TO BE REVIEWED, IS NOT GOOD DELETE SOMETHING FROM DATABASE, NEED TO CONSIDER CREATE A FLAG
#  TO SET INACTIVE
def delete_apply_to_job(userId, jobId):
    sql = """
            update VagasAplicadas set Ativo = 'F' where Id_Vaga = %d and Id_Candidato = %d
        """
    param = (jobId, userId)
    db.execute_delete(sql, param)
