import app.database.Database as db


def get_companies():
    sql = """
        SELECT  Id,
                Nome
        FROM Empresa
    """

    return db.execute_query_fetchall(sql, ())


def create_company(company_name):
    sql = """
        INSERT INTO Empresa (Nome)
        VALUES (?)
    """

    param = (company_name,)

    db.execute_insert(sql, param)


def update_company(company_id, company_name):
    sql = """
        UPDATE Empresa SET Nome = ? WHERE Id = ?
    """

    param = (company_name, company_id)

    db.execute_update(sql, param)


def delete_company(company_id):
    sql = """
        DELETE FROM Empresa WHERE Id = ?
    """

    param = (company_id,)

    db.execute_delete(sql, param)


def check_if_is_deletable(company_id):
    sql = """
        SELECT 1 FROM Usuario WHERE Id_Empresa = ?
    """

    param = (company_id,)

    return db.execute_query_fetchall(sql, param)