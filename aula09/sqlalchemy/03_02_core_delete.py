#!/usr/bin/python3

from sqlalchemy import update
from core import user_table, engine

con = engine.connect()
# atualizar = update(user_table).where(user_table.c.nome == 'Maria')
atualizar = update(user_table).where(user_table.c.id == 5)
commit = atualizar.values(nome='Chan Burzum')
result = con.execute(commit)
print(result.rowcount)
