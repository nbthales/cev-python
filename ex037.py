#DESAFIO 037
#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA
#PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DA CONVERSÃO:

#1 PARA BINÁRIO
#2 PARA OCTAL
#3 PARA HEXADECIMAL

numero = int(input('Digite um número inteiro: '))
esc = int(input('Escolha uma das bases para conversão:\n'
                '[ 1 ] converter para BINÁRIO\n'
                '[ 2 ] converter para OCTAL\n'
                '[ 3 ] converter para HEXADECIMAL\n'
                'Sua opção: '))

if esc == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif esc == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif esc == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção Inválida')
