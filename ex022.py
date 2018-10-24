#DESAFIO 022
#CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
#O NOME COM TODAS AS LETRAS MAIÚSCULAS
#O NOME COM TODAS MINÚSCULAS
#QUANTAS LETRAS AO TODOO SEM CONSIDERAR ESPAÇOS.
#QUANTAS LETRAS TEM O PRIMEIRO NOME.

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
