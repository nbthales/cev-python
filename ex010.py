#DESAFIO 010
#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA
#E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR
#CONSIDERE US$1,00 = R$ 3,27

din = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${} você pode comprar US${:.2f}'.format(din, din/3.27))
