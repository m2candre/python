#!/usr/bin/python3

import psycopg2

try:
    con = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux')
    cur = con.cursor()
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

try:
    cur.execute("insert into usuario (nome, dtnasc) values ('Pedro','1981-12-31')")
    cur.execute("insert into usuario (nome, dtnasc) values ('Jeferson','1999-12-31')")
    con.commit()
except Exception as e:
    con.rollback()
    print('Erro: {}'.format(e))
finally:
    cur.close()
    con.close()
