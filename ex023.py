#DESAFIO 023

#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA
#CADA UM DOS DIGITOS SEPARADOS.

#EX: DIGITE UM NÚMERO: 1834
#UNIDADE: 4
#DEZENAS: 3
#CENTENAS: 8
#MILHAR: 1

num = int(input('Informe um número: '))
#n = str(num)
#print('Analisando o número {}'.format(num))
#print('Unidade: {}'.format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))