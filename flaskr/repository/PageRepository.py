from flaskr.database import database as db


def get_all_pages_by_user_id(userId):
    sql = """
    select  Paginas.Id,
            PaginasInf.Nome,
            Paginas.Constante,
            Paginas.Ativo
    from    Paginas
    join PaginasInf
    on   PaginasInf.Id_Pagina = Paginas.Id
    join PermissaoPaginas
    on   PermissaoPaginas.Id_Pagina = Paginas.Id
    and  PermissaoPaginas.Id_Usuario = %d
    and  PermissaoPaginas.Permissao <> 0
    """
    return db.execute_query_fetchall(sql, userId)