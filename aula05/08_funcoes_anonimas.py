#!/usr/bin/python3

# Equivale ao lambda abaixo
# def soma(x, y):
#     return x + y

# print(soma(5,6)

a = lambda x, y: x + y
print(a(5,6))

print('-' * 50)

print((lambda x: x ** 2)(3))

print('-' * 50)

for x in range(1, 11):
    print((lambda x: x ** 2)(x))

print('-' * 50)

quadrado = []
for x in range(1, 11):
    quadrado.append((lambda x: x ** 2)(x))

print(quadrado)

print('-' * 50)

quadrado = list(map(lambda x: x ** 2, range(1, 11)))

print(quadrado)
