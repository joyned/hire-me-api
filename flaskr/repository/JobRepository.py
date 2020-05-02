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
        WHERE  Codigo = %d
    """
    param = (id)
    return db.execute_query_fetchone(sql, param)


def apply_to_job(userId, jobId):
    sql = """
        insert into VagasAplicadas (Id_Vaga, Id_Candidato) values (%d, %d)
    """
    param = (userId, jobId)
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
    AND VagasAplicadas.Id_Candidato = %d
    """
    param = (userId)
    return db.execute_query_fetchall(sql, param)