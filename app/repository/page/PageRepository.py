from app.database import database as db


def get_all_pages_by_user_id(user_profile_id):
    sql = """
    SELECT  Pagina.Id,
            Pagina.Constante,
            PaginaInf.Nome,
            Pagina.Icone,
            PerfilUsuarioPermissaoPagina.Permissao
    FROM    Pagina
    JOIN PaginaInf
        ON PaginaInf.Id_Pagina = Pagina.Id
    JOIN PerfilUsuarioPermissaoPagina
        ON PerfilUsuarioPermissaoPagina.Id_Pagina = Pagina.Id
    WHERE PerfilUsuarioPermissaoPagina.Permissao = 'T'
    AND   PerfilUsuarioPermissaoPagina.Id_Perfil_Usuario = %d
    """
    return db.execute_query_fetchall(sql, user_profile_id)


def check_permission(user_profile_id, page_id):
    sql = """
    SELECT  1
    FROM    PerfilUsuarioPermissaoPagina
    WHERE PerfilUsuarioPermissaoPagina.Id_Perfil_Usuario = %d
    AND PerfilUsuarioPermissaoPagina.Id_Pagina = %d
    AND PerfilUsuarioPermissaoPagina.Permissao = 'T'
    """
    param = (user_profile_id, page_id)
    return db.execute_query_fetchone(sql, param)


def insert_new_page(data):
    sql = """
        INSERT INTO Pagina (Constante, Ativo) VALUES (%s, %s)
    """
    param = (data.get('pageURL'), 'T')
    page_id = db.execute_insert(sql, param)

    sql = """
        INSERT INTO PaginaInf (Id_Pagina, Idioma, Nome) VALUES (%s, %s, %s)
    """
    param = (page_id, 'pt', data.get('pageName'))
    db.execute_insert(sql, param)

    return page_id


def insert_page_permission(page_id, user_profile_id):
    sql = """
        INSERT INTO PerfilUsuarioPermissaoPagina (Id_Pagina, Id_Perfil_Usuario, Permissao)
        VALUES (%d, %d, %s)
    """
    param = (page_id, user_profile_id, 'T')
    db.execute_insert(sql, param)
