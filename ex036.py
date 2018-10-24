#DESAFIO 036

#ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA
#A COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA
#CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.

#CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE
#EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO

vcasa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
mensal = vcasa / (anos*12)
salparc = salario * 0.3

if salparc < mensal:
    emprestimo = 'NEGADO'
else:
    emprestimo = 'APROVADO'

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(vcasa, anos, mensal))
print('Empréstimo {}!'.format(emprestimo))
