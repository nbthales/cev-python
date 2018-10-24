#DESAFIO 044

#ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO,
#CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:

#À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
#À VISTA NO CARTÃO: 5% DE DESCONTO
#EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
#3x OU MAIS NO CARTÃO: 20% DE JUROS

print('='*11, 'LOJAS TERRA', '='*11)
preco = float(input('Preço das compras: R$'))
opcao = int(input('FORMA DE PAGAMENTO\n'
                  '[ 1 ] à vista dinheiro/cheque\n'
                  '[ 2 ] à vista cartão\n'
                  '[ 3 ] 2x no cartão\n'
                  '[ 4 ] 3x ou mais no cartão\n'
                  'Qual é a opção? '))
if opcao == 1:
    novo = preco - (preco*0.1)
    print('Sua compra é de R${:.2f} vai custar R${:.2f} no final.'.format(preco, novo))
elif opcao == 2:
    novo = preco - (preco*0.05)
    print('Sua compra é de R${:.2f} vai custar R${:.2f} no final.'.format(preco, novo))
elif opcao == 3:
    parc = preco / 2
    print('Sua compra é de R${:.2f} e será parcelada em 2x de R${:.2f} SEM JUROS'.format(preco, parc))
elif opcao == 4:
    total = preco + (preco*0.2)
    parc = int(input('Quantas parcelas? '))
    tp = total / parc
    print('Sua compra de R${:.2f} vai custar R${:.2f}\n'
          'Sua compra seráparcelada em {}x de R${:.2f} COM JUROS'.format(preco, total, parc, tp))
else:
    print('Opção Inválida!')
