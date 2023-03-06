# encoding: utf8

from django.db import connection


def named_tuple_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def sql_query(sql):
    with connection.cursor() as cur:
        cur.execute(sql)
        return named_tuple_fetchall(cur)


def sql_insert_or_update(sql):
    with connection.cursor() as cur:
        return cur.execute(sql)
