import app.database.Database as db
from app.model.context.HireMeContext import HireMeContext


def check_if_email_exists(email):
    sql = """
        SELECT 1 FROM Usuario WHERE Email = ?
    """

    param = (email,)

    return db.execute_query_fetchone(sql, param)


def update_password_by_email(email, new_password):
    sql = """
        UPDATE Usuario SET Senha = ? WHERE Email = ?
    """

    param = (new_password, email)

    db.execute_update(sql, param)


def update_password_by_user_id(context: HireMeContext, new_password):
    sql = """
        UPDATE Usuario SET Senha = ? WHERE Id = ?
    """

    param = (new_password, context.user_id)

    db.execute_update(sql, param)


def get_hash_password_by_user_id(context: HireMeContext):
    sql = """
        SELECT Senha FROM Usuario WHERE Id = ? 
    """

    param = (context.user_id,)

    return db.execute_query_fetchone(sql, param)
