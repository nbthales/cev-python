#DESAFIO 066

# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO
# O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999,
# QUE É A CONDIÇÃO DE PARADA. NO FINAL, MOSTRE QUANTOS NÚMEROS
# FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES
# (DESCONSIDERANDO O FLAG)

soma = cont = 0
while True:
    valor = int(input('Digite um valor (999 para parar): '))
    if valor == 999:
        break
    soma += valor
    cont += 1
print(f'A soma dos {cont} valores foi {soma}!')
