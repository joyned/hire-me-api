import pymssql
import yaml

db_properties = yaml.load(open('flaskr/database/db_properties.yml'))

connection = {
    'host': db_properties['user']['host'],
    'username': db_properties['user']['username'],
    'password': db_properties['user']['password'],
    'db': db_properties['user']['db']
}

conn = pymssql.connect(connection['host'], connection['username'], connection['password'], connection['db'])
cursor = conn.cursor()


def close_connection():
    def decorator_func(func):
        def wrapper_func(*args, **kwargs):
            # Invoke the wrapped function first
            retval = func(*args, **kwargs)
            # Now do something here with retval and/or action
            close()
            return retval

        return wrapper_func

    return decorator_func


def close():
    cursor.close()


def execute_query_fetchall(sql, param):
    cursor.execute(sql, param)
    return cursor.fetchall()


def execute_query_fetchone(sql, param):
    cursor.execute(sql, param)
    return cursor.fetchone()


def execute_insert(sql, param):
    cursor.execute(sql, param)
    conn.commit()


def execute_delete(sql, param):
    cursor.execute(sql, param)
    conn.commit()
