# DESAFIO 081

# CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR
# EM UMA LISTA.

# DEPOIS DISSO, MOSTRE:

# A) QUANTOS NÚMEROS FORAM DIGITADOS.
# B) A LISTA DE VALORES, ORDENADA DE FORMA DECRESCENTE.
# C) SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA.

valor = []
while True:
    valor.append(int(input('Digite um valor: ')))

    op = str(input('Quer continuar? [S/N] ')).lower()

    if op in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valor)} elementos')
valor.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valor}')
if 5 in valor:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
