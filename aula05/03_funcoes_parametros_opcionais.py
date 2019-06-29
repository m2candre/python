#!/usr/bin/python3

def boas_vindas(nome=''):
    if nome != '':
        print('Seja bem vindo {}!'.format(nome))

boas_vindas()
boas_vindas('Marcos')
