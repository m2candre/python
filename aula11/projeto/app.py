#!/usr/bin/python3

import modulos.banco as banco
import threading

if __name__ == '__main__':
    user = input('Nickname: ')

    try:
        f = threading.Thread(target = banco.buscda_mensagem)
        f.start()
    except Exception as e:
        print('Falha ao criar a thread: {}'.format(e))

    while f.isAlive:
        mens = input()
        banco.cadastrar_mensagem(user, mens)
