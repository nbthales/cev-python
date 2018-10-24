#DESAFIO 015
#ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO
#ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO
#A PAGAR, SABENDO QUE O CARRO CUSTA r$60 POR DIA E R$0.15 POR KM RODADO.

dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
print('O total a pagar é de R${:.2f}'.format((dias*60)+(km*0.15)))
