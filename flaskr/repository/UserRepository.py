from flaskr.database import database as db


def check_if_user_exists_on_database(user):
    sql = "select 1 from Usuario where Usuario = %s"
    param = (user)
    return db.execute_query_fetchone(sql, param)


def insert_new_user(user, pwd):
    sql = "insert into Usuario values (%s, %s, 2)"
    param = (user, pwd)
    db.execute_insert(sql, param)


def get_user_by_name(user):
    sql = "select Usuario.codigo, Usuario.usuario, Usuario.senha, Candidato.Nome" \
          " from Usuario " \
          " join Candidato on Candidato.Cod_Usuario = Usuario.Codigo"\
          " where Usuario = %s"
    param = (user)
    return db.execute_query_fetchone(sql, param)