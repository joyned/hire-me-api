from app.database import Database as db


def get_user_by_email(email):
    sql = """
        SELECT  Usuario.Id, 
                Usuario.Email, 
                Usuario.Senha,
                Usuario.Id_Perfil_Usuario,
                Pessoa.Nome, 
                Pessoa.Id 'Id_Pessoa',
                Usuario.Id_Empresa
        FROM    Usuario
            JOIN Pessoa 
                ON Pessoa.Id_Usuario = Usuario.Id
        WHERE Usuario.Email = ?
    """

    param = (email)

    return db.execute_query_fetchone(sql, param)
