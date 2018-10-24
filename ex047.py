#DESAFIO 047

#CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NÚMEROS
#PARES QUE ESTÃO NO INTERVALO ENTRE 1 E 50.

for c in range(0, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('Acabou')