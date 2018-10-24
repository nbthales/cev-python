#DESAFIO 059

# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM
# MENU NA TELA:

# [ 1 ] SOMAR
# [ 2 ] MULTIPLICAR
# [ 3 ] MAIOR
# [ 4 ] NOVOS NÚMEROS
# [ 5 ] SAIR DO PROGRAMA

# SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA
# EM CADA CASO.
from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''---------------------
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = v1 + v2
        print('A soma entre {} e {} é {}'.format(v1, v2, soma))
    elif opcao == 2:
        multi = v1 * v2
        print('A multiplicação entre {} e {} é {}'.format(v1, v2, multi))
    elif opcao == 3:
        maior = v1
        if v2 > v1:
            maior = v2
        print('O maior número entre {} e {} é {}'.format(v1, v2, maior))
    elif opcao == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando programa...')
    else:
        print('Opção Inválida!')
    sleep(2)
print('Fim do programa! volte Sempre!')
