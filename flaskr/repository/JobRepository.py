from flaskr.database import database as db


def get_jobs():
    sql = """
        SELECT Codigo,
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
        SELECT Codigo,
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
