#CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO
#TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA
#EX: DIGITE UM NÚMERO: 6.127
#O NÚMERO 6.127 TEM A PARTE INTEIRA 6.

from math import trunc
num = float(input('Digite um número real qualquer: '))
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))

print('O número {} tem a parte inteira {}'.format(num, int(num)))
