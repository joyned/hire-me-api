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

