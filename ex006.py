#DESAFIO 006
#CRIE UM ALGORITMO QUE LEIA UM NÚMERO E
#MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA

n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, n*2))
print('O triplo de {} vale {}.'. format(n, n*3))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(n, n**(1/2)))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(n, pow(n, (1/2))))
