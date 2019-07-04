#!/usr/bin/python3

# JSON - JavaScript object notation

import json

pessoas = [
    {
        'nome'  : 'Philadelpho',
        'dtnasc': '1937-06-12'
    },
    {
        'nome'  : 'Philomena',
        'dtnasc': '1928-07-15'
    }
]

print('-' * 50)

strJson = json.dumps(pessoas)

print('list[dist]<=>json')
print(type(strJson))
print(strJson)

print('-' * 50)

dicionario = json.loads(strJson)

print('icon<=>list[dict]')
print(type(dicionario))
print(dicionario)

print('-' * 50)

