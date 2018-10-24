# DESAFIO 065

# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO
# NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS VALORES
# E QUAL FOI O MAIOR E O MENOR VALORES LIDOS. O PROGRAMA DEVE
# PERGUNTAR AO USUÁRIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR
# VALORES

opcao = 'S'
cont = soma = maior = menor = 0
while opcao == 'S':
    numero = float(input('Digite um número: '))
    cont += 1
    soma += numero
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    opcao = input('Deseja Continuar? [S/N] ').upper().strip()[0]
media = soma / cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
