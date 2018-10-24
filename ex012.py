#DESAFIO 012
#FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE
#SEU NOVO PREÇO, COM 5% DE DESCONTO.
preco = float(input('Qual é o preço do produto? R$'))
print('O produto que custava R${}, na promoção com desconto de 5% '
      'vai custar R${:.2f}.'.format(preco, preco-(preco*0.05)))
