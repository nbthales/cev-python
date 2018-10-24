#DESAFIO 031
#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM.
#CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA VIAGENS DE ATÉ 200KM
#E R$0,45 PARA VIAGENS MAIS LONGAS

dist = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}km.'.format(dist))

'''if dist <= 200:
    resultado = dist * 0.50
else:
    resultado = dist * 0.45'''

resultado = dist * 0.5 if dist <= 200 else dist * 0.45

print('E o preço da sua passagem será de R${:.2f}'.format(resultado))
