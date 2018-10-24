#DESAFIO 018

#FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE O VALOR
#DO SENO, COSSENO E TANGENTE DESSE ÂNGULO

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, sin(radians(angulo))))
print('O ângulo de {} tem o COESSNO de {:.2f}'.format(angulo, cos(radians(angulo))))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tan(radians(angulo))))
