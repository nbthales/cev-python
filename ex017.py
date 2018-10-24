#DESAFIO 017

#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM
#TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA

from math import hypot
cop = float(input('Digite o comprimento do cateto oposto: '))
cad = float(input('Digite o comprimento do cateto adjacente: '))
#hi = (cop ** 2 + cad ** 2) ** (1/2)
hi = hypot(cop, cad)
print('A hipotenusa vai medir {:.2f}'.format(hi))
