# DESAFIO 100

# FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA
# NÚMEROS E DUAS FUNÇÕES CHAMADAS sorteia() E
# somaPar(). A PRIMEIRA FUNÇÃO VAI SORTEAR 5
# NÚMEROS E VAI COLOCÁ-LOS DENTRO DA LISTA E
# A SEGUNDA FUNÇÃO VAI MOSTRAR A SOMA ENTRE
# TODOS OS VALORES PARES SORTEADOS PELA FUNÇÃO
# ANTERIOR.

from random import randint
from time import sleep
numeros = list()


def sorteia():
    for c in range(0, 5):
        numeros.append(randint(0, 10))
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in numeros:
        sleep(0.3)
        print(c, end=' ')
    print('PRONTO!')


def somaPar():
    somaPares = 0
    for c in numeros:
        if c % 2 == 0:
            somaPares += c
    print(f'Somando os valores pares de {numeros}, temos {somaPares}')


sorteia()
somaPar()
