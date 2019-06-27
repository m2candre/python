#!/usr/bin/python3

for x in range(11):
    print(x)

print('--------------------')

#range(inicio, fim)
for x in range(1,11):
    print(x)

print('--------------------')

#range(inicio, fim, incremento)
for x in range(2,11,2):
    print(x)

print('--------------------')

#range(inicio, fim, incremento) - Contagem decrescente
for x in range(10,1,-2):
    print(x)

print('--------------------')

#range(inicio, fim, incremento) - Imprimendo caracteres
for x in range(97,97 + 26):
    print(chr(x))

print('--------------------')

#range(inicio, fim, incremento) - Criando uma lista
letras = []
for x in range(97,97 + 26):
    letras.append(chr(x))

print(letras)

print('--------------------')

frutas = ["Manga","Abacaxi","Uva"]

for num, item in enumerate(frutas):
    print("{} está na posição {}".format(item,num))
