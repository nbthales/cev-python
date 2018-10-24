#DESAFIO 030
#CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU IMPAR

numero = int(input('Me diga um número qualquer: '))
n = numero % 2
if n == 0:
    resp = 'PAR'
else:
    resp = 'ÍMPAR'
print('O número {} é {}!'.format(numero, resp))
