import pyodbc

from app.utils.resource import ResourceUtil

db_properties = ResourceUtil.get_resource_file('db_properties.yml')
environment = ResourceUtil.get_resource_file('environment.yml')

connection = {
    'host': db_properties['user']['host'],
    'username': db_properties['user']['username'],
    'password': db_properties['user']['password'],
    'db': db_properties['user']['db'],
    'driver': db_properties['user']['driver']
}

connection_local = {
    'host': 'localhost',
    'username': 'SA',
    'password': '$b4tr0x2568251$',
    'db': 'HireMeRemodel',
    'driver': db_properties['user']['driver']
}

prod = bool(environment['environment']['production'])


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
    return pyodbc.connect(
        'DRIVER=' + connection['driver'] + ';SERVER=' + connection['host'] + ';PORT=1433;DATABASE=' + connection[
            'db'] + ';UID=' + connection['username'] + ';PWD=' + connection['password'])


def create_local_connection():
    return pyodbc.connect(
        'DRIVER=' + connection_local['driver'] + ';SERVER=' + connection_local['host'] + ';PORT=1433;DATABASE=' +
        connection_local['db'] + ';UID=' + connection_local['username'] + ';PWD=' + connection_local['password'])


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
    last_row_id = get_last_inserted_row_id(cursor)
    conn.commit()
    conn.rollback()
    conn.close()
    return last_row_id


def get_last_inserted_row_id(cursor):
    cursor.execute("SELECT @@IDENTITY")
    row = cursor.fetchone()
    return row[0]


def execute_update(sql, param):
    execute_insert(sql, param)


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
    cursor.fetchall()
    res = int(len(cursor.fetchall()))
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
