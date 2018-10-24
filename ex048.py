#DESAFIO 048

#FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS
#ÍMPARES QUE SÃO MÚLTIPLOS DE TRÊS E QUE SE ENCONTRAM NO
#INTERVALO DE 1 ATÉ 500.

soma = 0
total = 0
for cont in range(1, 500):
    if cont % 2 == 1:
        if cont % 3 == 0:
            soma += 1
            total += cont
            #print(cont, end=' ')

print('\nA soma de todos os {} valores solicidados é {}'.format(soma, total))

