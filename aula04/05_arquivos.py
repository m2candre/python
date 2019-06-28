#!/usr/bin/python3

arquivo = open('frutas.txt', 'w')
arquivo.write('Banana\n')
arquivo.close()

with open('frutas.txt', 'a') as arquivo:
    arquivo.write('Limão\n')
    arquivo.write('Melancia\n')

with open('frutas.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha)

nomes = ['João', 'Maria', 'Pedro']
with open('nomes.txt', 'x') as arquivo:
    arquivo.writelines(nomes)

with open('nomes.txt', 'w') as arquivo:
    for nome in nomes:
        arquivo.write(nome + '\n')
        