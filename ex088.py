# DESAFIO 088

# FAÇA UM PROGRAMA QUE AJUDE UM JOGADOR DA MEGA SENA A
# CRIAR PALPITES. O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS
# SERÃO GERADOS E VAI SORTEAR 6 NÚMEROS ENTRE 1 E 60
# PARA CADA JOGO, CADASTRANDO TUDO EM UMA LISTA COMPOSTA

from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('      JOGA NA  MEGA SENA      ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 4, '< BOA SORTE! >', '=-' * 4)
