from flaskr.database import database as db


def get_all_pages_by_user_id(userId):
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
    return db.execute_query_fetchall(sql, userId)