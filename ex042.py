#DESAFIO 042
#REFAÇA O DESAFIO 035 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO
#DE MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO:
#- EQUILÁTERO: TODOS LADOS IGUAIS
#- ISÓCELES: DOIS LADOS IGUAIS
#- ESCALENO: TODOS OS LADOS DIFERENTES

print('-='*15, '\nAnalisador de Triângulos 2.0\n', end='' '-='*15)
r1 = float(input('\nPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 !=r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES')
else:
    print('NÃO FORMAM UM TRIÂNGULO!')
