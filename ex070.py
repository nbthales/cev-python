#DESAFIO 070

# CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS
# O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR.
# NO FINAL, MOSTRE:

# A) QUAL É O TOTAL GASTO NA COMPRA.
# B) QUANTOS PRODUTOS CUSTAM MAIS DE R$ 100,00
# C) QUAL É O NOME DO PRODUTO MAIS BARATO.

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
