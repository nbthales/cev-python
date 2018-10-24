#DESAFIO 035
#DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUÁRIO SE ELAS
#PODEM OU NÃO FORMAR UM TRIÂNGULO

print('-='*12, '\nAnalisador de Triângulos\n', end='' '-='*12)
r1 = float(input('\nPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    resp = ('PODEM FORMAR')
else:
    resp = ('NÃO FORMAM')

print('Os segmentos acima {} triângulo!'.format(resp))
