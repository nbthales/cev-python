#DESAFIO 004
#FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO
#PRIMITIVO E TODAS AS INFORMAÇÕES SOBRE ELE.

algo = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(algo)))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É um número? {}'.format(algo.isnumeric()))
print('É alfabético? {}'.format(algo.isalpha()))
print('É alfanumérico? {}'.format(algo.isalnum()))
print('Está em maiúsculas? {}'.format(algo.isupper()))
print('Está em minúsculas? {}'.format(algo.islower()))
print('Está capitalizada? {}'.format(algo.istitle()))
