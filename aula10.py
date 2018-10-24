#nome = str(input('Qual é o seu nome? '))
#if nome == 'Thales':
#    print('Seu nome é lindo!')
#else:
#    print('Seu nome é normal!')
#print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
#if m >= 7:
#    frase = 'está aprovado'
#else:
#    frase = 'está de recuperação'
print('A sua média foi {:.1f} e você'.format(m), end='')
print(' está aprovado' if m >= 7 else (' está de recuperação'))