from app.database import database as db


def register_new_user(user):
    db.execute_procedure('P$Register', user)


def check_if_email_exists(email):
    sql = """
    select 1 from Usuario where email = %s
    """

    return db.execute_query_fetchone(sql, (email))
