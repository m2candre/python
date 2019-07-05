#!/usr/bin/python3

import psycopg2

try:
    con = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux')
    cur = con.cursor()
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

try:
    cur.execute("select * from usuario;")
    # print(cur.fetchone())
    print(cur.fetchall())
    con.commit()
except Exception as e:
    print('Erro: {}'.format(e))
finally:
    cur.close()
    con.close()
