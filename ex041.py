#DESAFIO 041

#A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE
#LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA,
#DE ACORDO COM A IDADE:

#- ATÉ 9 ANOS: MIRIM
#- ATÉ 14 ANOS: INFANTIL
#- ATÉ 19 ANOS: JUNIOR
#- ATÉ 20 ANOS: SÊNIOR
#- ACIMA: MASTER

from datetime import date

atual = date.today().year
nasci = int(input('Ano de Nascimento: '))
idade = atual - nasci
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    c = 'MIRIM'
elif idade > 9 and idade <= 14:
    c = 'INFANTIL'
elif idade > 14 and idade <= 19:
    c = 'JUNIOR'
else:
    c = 'MASTER'

print('Classificação: {}'.format(c))
