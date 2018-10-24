'''for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('FIM')'''

'''c = 1
while c < 10:
    print(c)
    c = c +1
print('FIM')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''

n = 1
par = impar = 0
contp = conti = 0
while n != 0:
    n = int(input('Digite o valor: '))
    if n != 0:
        if n % 2 == 0:
            par += n
            contp += 1
        if n % 2 == 1:
            impar += n
            conti += 1
print('Você digitou {} pares e a soma é {}'.format(contp, par))
print('Você digitou {} ímpares e soma é {}'.format(conti, impar))

