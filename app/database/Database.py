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
    'db': 'HireMeRemodel'
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
    # return pymssql.connect(connection['host'], 1433, connection['username'], connection['password'], connection['db'])
    return pyodbc.connect('DRIVER=' + connection['driver'] + ';SERVER=' + connection['host'] + ';PORT=1433;DATABASE=' + connection['db'] + ';UID=' + connection['username'] + ';PWD=' + connection['password'])


def create_local_connection():
    # return pymssql.connect(connection_local['host'], connection_local['username'], connection_local['password'], connection_local['db'])
    return 0


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
    last_row_id = cursor.lastrowid
    conn.rollback()
    conn.close()
    return last_row_id


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
    res = int(cursor.rowcount)
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
