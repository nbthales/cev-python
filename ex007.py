#DESAFIO 007
#DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS
#DE UM ALUNO, CALCULE E MOSTRE A SUA MEDIA

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, (n1+n2)/2))
