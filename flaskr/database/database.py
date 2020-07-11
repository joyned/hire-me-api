import pymssql
import yaml

db_properties = yaml.load(open('flaskr/database/db_properties.yml'))

connection = {
    'host': db_properties['user']['host'],
    'username': db_properties['user']['username'],
    'password': db_properties['user']['password'],
    'db': db_properties['user']['db']
}

connection_local = {
    'host': 'localhost',
    'username': 'SA',
    'password': '$b4tr0x2568251$',
    'db': 'HireMe'
}

prod = True


def db_connection():
    def decorator_func(func):
        def wrapper_func(*args, **kwargs):
            # Invoke the wrapped function first
            retval = func(*args, **kwargs)
            # Now do something here with retval and/or action
            return retval

        return wrapper_func

    return decorator_func


def create_connection():
    return pymssql.connect(connection['host'], connection['username'], connection['password'], connection['db'])


def create_local_connection():
    return pymssql.connect(connection_local['host'], connection_local['username'], connection_local['password'],
                           connection_local['db'])


def execute_query_fetchall(sql, param):
    if prod:
        conn = create_connection()
    else:
        conn = create_local_connection()
    cursor = conn.cursor()
    cursor.execute(sql, param)
    res = cursor.fetchall()
    conn.close()
    return res


def execute_query_fetchone(sql, param):
    if prod:
        conn = create_connection()
    else:
        conn = create_local_connection()
    cursor = conn.cursor()
    cursor.execute(sql, param)
    res = cursor.fetchone()
    conn.close()
    return res


def execute_insert(sql, param):
    if prod:
        conn = create_connection()
    else:
        conn = create_local_connection()
    cursor = conn.cursor()
    cursor.execute(sql, param)
    conn.commit()
    conn.close()


def execute_delete(sql, param):
    if prod:
        conn = create_connection()
    else:
        conn = create_local_connection()
    cursor = conn.cursor()
    cursor.execute(sql, param)
    conn.commit()
    conn.close()


def execute_count_lines(sql, param):
    if prod:
        conn = create_connection()
    else:
        conn = create_local_connection()
    cursor = conn.cursor()
    cursor.execute(sql, param)
    res = cursor.rowcount()
    conn.close()
    return res


def execute_procedure(procedure, param):
    if prod:
        conn = create_connection()
    else:
        conn = create_local_connection()
    cursor = conn.cursor()
    cursor.callproc(procedure, param)
    conn.commit()
    conn.close()
