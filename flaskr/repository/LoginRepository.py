from flaskr.database import database as db


def get_user_by_email(email):
    sql = """
        SELECT  Usuario.Id, 
                Usuario.Email, 
                Usuario.Senha,
                Usuario.Id_Perfil_Usuario,
                Pessoa.Nome, 
                Pessoa.Id 'Id_Pessoa'
        FROM    Usuario
            JOIN Pessoa 
                ON Pessoa.Id_Usuario = Usuario.Id
        WHERE Usuario.Email = %s
    """

    return db.execute_query_fetchone(sql, email)
