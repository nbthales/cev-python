#DESAFIO 045

#CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOKENPÔ COM VOCÊ
from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('Suas opções:\n'
        '[ 0 ] PEDRA\n'
        '[ 1 ] PAPEL\n'
        '[ 2 ] TESOURA\n')
jogador = int(input('Qual é a sua jogada? '))

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*20)
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*20)

if comp == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif comp == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif comp == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
