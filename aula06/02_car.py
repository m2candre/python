#!/usr/bin/python3

class Carro():
    __priprietario = 'Marcos'

    def __ini__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.combustivel = 'gasolina'


    def __del__(self):
        print('Método destrutor executor!')


    def acelerar(self):
        print('Vruuun')


    def freiar(self):
        print('Freiando...')


    def getProprietario(self):
        return self.__priprietario


    def setProprietario(self, proprietario):
        self.__priprietario = proprietario


class CarroEletrico(Carro):
    def __ini__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.combustivel = 'elétrico'


    def acelerar(self):
        print('Shiiiiffffff.....')

car1 = Carro('BMW', 'i320', 2016)
print(car1.modelo, car1.combustivel)
car1.acelerar()

print('Proprietário', car1.getProprietario(), sep='\n')
print('-' * 50)

car2 = CarroEletrico('Chevrolet', 'Bolt', 2018)

print('Proprietário', car2.getProprietario(), sep='\n')
print('-' * 50)

proprietario = input('Informe o proprietário do carro: ')

car2.setProprietario(proprietario.strip())
