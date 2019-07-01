#!/usr/bin/python3

def cadastro(**pessoa):
    # return pessoa
    # return type(pessoa)
    return 'O usuário {} {} foi cadastrado com sucesso'.format(pessoa['nome'],pessoa['sobrenome'])

print(cadastro(nome='Marcos', sobrenome='Souza', idade=41))


def cadastro(pessoa):
    # return pessoa
    # return type(pessoa)
    return 'O usuário {} {} foi cadastrado com sucesso'.format(pessoa['nome'],pessoa['sobrenome'])

pessoa = {
    'nome': 'Marcos',
    'sobrenome': 'André',
    'idade': 43
}

print(cadastro(pessoa))

