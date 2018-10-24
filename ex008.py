#DESAFIO 008
#ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS
#E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS

dis = float(input('Uma distância em metros: '))
print('A medida de {:.1f}m corresponde a'.format(dis))
print('{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(dis/1000, dis/100, dis/10,
                                                               dis*10, dis*100, dis*1000))
