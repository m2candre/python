#!/usr/bin/python3

import MySQLdb

try:
    con = MySQLdb.connect(host='localhost', user='admin', password='4linux', db='projeto')
    cur = con.cursor()
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

try:
    cur.execute("delete from usuario where id=4;")
    con.commit()
except Exception as e:
    con.rollback()
    print('Erro: {}'.format(e))
finally:
    cur.close()
    con.close()
