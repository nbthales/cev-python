# DESAFIO 084

# FAÇA UM PROGRAMA QUE LEIA O NOME E PESO DE VÁRIAS PESSOAS,
# GUARDANDO TUDO EM UMA LISTA. NO FINAL, MOSTRE:

# A) QUANTAS PESSOAS FORAM CADASTRADAS.
# B) UMA LISTAGEM COM AS PESSOAS MAIS PESADAS.
# C) UMA LISTAGEM COM AS PESSOAS MAIS LEVES.

temp = list()
princ = list()
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()

    opcao = str(input('Quer continuar? [S/N] '))
    if opcao in 'nN':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
