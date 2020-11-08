from app.database import Database as db


def register_new_user(user):
    sql = """
        DECLARE @return_value int;
        EXEC    @return_value = P$Register ? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,?;
        SELECT  'Return Value' = @return_value;
    """

    return db.execute_insert(sql, user)


def check_if_email_exists(email):
    sql = """
    SELECT 1 FROM Usuario WHERE email = ?
    """

    return db.execute_query_fetchone(sql, (email))


def insert_person_professional_history(professional_history):
    sql = """    
        INSERT INTO PessoaHistoricoProfissional (Id_Pessoa, Empresa, Cargo, Descricao, Data_Entrada, Data_Saida, Trabalha_Atualmente)
            VALUES(?,?,?,?,?,?,?)
    """

    return db.execute_insert(sql, professional_history)
