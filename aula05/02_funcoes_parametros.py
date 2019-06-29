#!/usr/bin/python3

def boas_vindas(nome):
    print('Seja bem vindo {}!'.format(nome))

boas_vindas('Marcos')

nome = input('Informe seu nome: ')
boas_vindas(nome)

boas_vindas()