from flaskr.database import database as db


def get_user_by_name(user):
    sql = """
    select Usuario.codigo, Usuario.usuario, Usuario.senha, Candidato.Nome, Candidato.Id Id_Candidato
    from Usuario 
    join Candidato on Candidato.Cod_Usuario = Usuario.Codigo
    where Usuario = %s
    """
    param = (user)
    return db.execute_query_fetchone(sql, param)


def get_users_profiles():
    sql = """
        select id, constante from perfilusuario
    """
    return db.execute_query_fetchall(sql, ())
