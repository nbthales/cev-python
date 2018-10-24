# DESAFIO 078

# FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E
# GUARDE-OS EM UMA LISTA.

# NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR
# DIGITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA.

listanum = []
mai = men = 0

for cont in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {cont+1}: ')))
    if cont == 0:
        mai = men = listanum[cont]
    else:
        if listanum[cont] > mai:
            mai = listanum[cont]
        if listanum[cont] < men:
            men = listanum[cont]
print('-=' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
