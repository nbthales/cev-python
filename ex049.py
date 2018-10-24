#DESAFIO 049

#REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO
#QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR.

n = int(input('Digite um número para ver sua tabuada: '))
print('='*12)
for c in range(0, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))
print('='*12)
