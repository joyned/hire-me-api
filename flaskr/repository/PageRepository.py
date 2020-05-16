from flaskr.database import database as db


def get_all_pages_by_user_id(user_id):
    sql = """
    SELECT  Paginas.Id,
            Paginas.Constante,
            PaginasInf.Nome,
            PermissaoPaginas.Permissao
    FROM    Paginas
    JOIN PaginasInf
        ON PaginasInf.Id_Pagina = Paginas.Id
    JOIN PermissaoPaginas
        ON PermissaoPaginas.Id_Pagina = Paginas.Id
    WHERE PermissaoPaginas.Permissao = (SELECT Usuario.Id_Perfil_Usuario FROM Usuario WHERE Codigo = %d)
    """
    return db.execute_query_fetchall(sql, user_id)


def check_permission(user_id, page):
    sql = """
    SELECT 1
    FROM    Usuario
    JOIN PermissaoPaginas
        ON PermissaoPaginas.Permissao = Usuario.Id_Perfil_Usuario
    JOIN Paginas
        ON Paginas.Constante = %s
    WHERE Usuario.Codigo = %d
    AND Paginas.Id = PermissaoPaginas.Id_Pagina
    """
    param = (user_id, page)
    return db.execute_query_fetchone(sql, param)
