from app.database import Database as db


def get_user_by_name(user):
    sql = """
    select Usuario.codigo, Usuario.usuario, Usuario.senha, Candidato.Nome, Candidato.Id Id_Candidato
    from Usuario 
    join Candidato on Candidato.Cod_Usuario = Usuario.Codigo
    where Usuario = ?
    """
    param = (user)
    return db.execute_query_fetchone(sql, param)


def get_users_profiles():
    sql = """
        select id, constante from perfilusuario
    """
    return db.execute_query_fetchall(sql, ())


def get_current_password_hash(user_id):
    sql = """
        SELECT Senha FROM Usuario WHERE Id = ?
    """

    return db.execute_query_fetchone(sql, user_id)


def update_user_password(user_id, pwd):
    sql = """
        UPDATE Usuario SET Senha = ? WHERE Id = ?
    """

    param = (pwd, user_id)

    db.execute_insert(sql, param)
