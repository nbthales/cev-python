#DESAFIO 029

#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
#SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
#A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE

vel = float(input('Qual é a velocidade atual do carro? '))

if vel > 80:
    multa = (vel - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')