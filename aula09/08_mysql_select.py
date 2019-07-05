#!/usr/bin/python3

import MySQLdb

try:
    con = MySQLdb.connect(host='localhost', user='admin', password='4linux', db='projeto')
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
