#DESAFIO 067

# FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS,
# UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUÁRIO.
# O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO
# FOR NEGATIVO

while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    print('-'*35)

    for c in range(1, 11):
        print(f'{valor} x {c} = {valor*c}')

    print('-'*35)
print('PROGRAMA ENCERRADO.')