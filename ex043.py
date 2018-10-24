#DESAFIO 043

#DESENVOLVA UMA LÓGIA QUE LEIA O PESO E A ALTURA DE UMA PESSOA,
#CALCULE SEU IMC E MOSTRE SEU STATUS, DE ACORDO COM A TABLEA
#ABAIXO:

#ATUALIZADO

#Abaixo de 17	Muito abaixo do peso
#Entre 17 e 18,49	Abaixo do peso
#Entre 18,5 e 24,99	Peso normal
#Entre 25 e 29,99	Acima do peso
#Entre 30 e 34,99	Obesidade I
#Entre 35 e 39,99	Obesidade II (severa)
#Acima de 40	Obesidade III (mórbida)

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
IMC = peso / (altura**2)
print('O IMC dessa pessoa é de {:.2f}'.format(IMC))

if IMC < 17:
    print('Muito abaixo do peso')
elif IMC >= 17 and IMC <= 18.49:
    print('Abaixo do peso')
elif IMC >= 18.5 and IMC <= 24.99:
    print('Peso normal')
elif IMC >= 25 and IMC <= 29.99:
    print('Acima do peso')
elif IMC >= 30 and IMC <= 34.99:
    print('Obesidade I')
elif IMC >= 35 and IMC <= 39.99:
    print('Obesidade II (severa)')
else:
    print('Obesidade III (mórbida)')