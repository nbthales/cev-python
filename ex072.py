# DESAFIO 072

# CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE
# PREENCHIDA COM UMA CONTAGEM POR EXTENSO, DE ZERO
# A VINTE.

# SEU PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO
# (ENTRE 0 E 20) E MOSTRÁ-LO POR EXTENSO.

txt = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
       'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
       'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if numero >= 0 and numero <= 20:
        print(f'Você digitou o número {txt[numero]}')
        break
    else:
        print('Tente novamente. ', end='')
