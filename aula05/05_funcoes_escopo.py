#!/usr/bin/python3

nome = 'Anônimo'

def boas_vindas():
    # global nome
    nome = 'Marcos'
    print('Seja bem vindo {}!'.format(nome))

boas_vindas()

print(nome)
