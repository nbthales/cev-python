#DESAFIO 051

#DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE
#UMA PA. NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO.

print('='*30, '\n{:^30}'.format('10 TERMOS DE UM PA'), '\n'+'='*30)

numero = int(input('Primeiro termo: '))
razao = int(input(('Razão: ')))
decimo = numero + (10 - 1) * razao

for c in range(numero, decimo, razao):
    print('{} '.format(c), end=' > ')
print('ACABOU')
