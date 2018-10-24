#DESAFIO 025
#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA
#TEM "SILVA" NO NOME.

nome = str(input('Qual é o seu nome completo? ')).upper().lower()
print('Seu nome tem Silva? {}'.format('silva' in nome))
