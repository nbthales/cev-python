#DESAFIO 039

#FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E
#INFORME, DE ACORDO COM SUA IDADE:

#- SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR.
#- SE É A HORA DE SE ALISTAR.
#- SE JÁ PASSOU DO TEMPO DO ALISTAMENTO.

#SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU
#QUE PASSOU DO PRAZO.

from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    resta = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(18-idade))
    print('Seu alistamento será em {}.'.format(atual+resta))
else:
    saldo = idade - 18
    ano = atual - saldo
    print('Você já deveria ter se alistado há {} anos!'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))

