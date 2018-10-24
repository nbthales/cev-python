#DESAFIO 058

#MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR
#VAI PENSAR EM UM NÚMERO ENTRE 0 A 10. SÓ QUE
#AGORA O JOGADOR VAI TENTAR ADVINHAR ATÉ ACERTAR,
#MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS
#PARA VENCER.

from random import randint

computador = randint(0, 5)
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 5.\n'
      'Será que você consegue adivinhar qual foi?')

numero = int(input('Qual é seu palpite? '))

qntd = 1
while numero != computador:
    if numero < computador:
        print('Mais... ', end='')
    elif numero > computador:
        print('Menos...', end='')
    numero = int(input('Tente mais uma vez: '))
    qntd += 1

print('\nVocê acertou com {} tentativas!\n'
      'Eu estava pensando no {}!!!'.format(qntd, computador))

