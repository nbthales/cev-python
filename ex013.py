#DESAFIO 013
#FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO
#E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO.

salario = float(input('Qual é o salário do Funcionário? R$'))
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, '
      'passa a receber R${:.2f}!'.format(salario, salario+(salario*0.15)))
