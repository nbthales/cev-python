#DESAFIO 054

#CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS.
#NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A
#MAIORIDADE E QUANTAS JÁ SÃO MAIORES.

from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade > 18:
        maior += 1
    else:
        menor += 1

print('\nAo todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
