#DESAFIO 040

#CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA
#MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL, DE ACORDO COM A MÉDIA
#ATINGIDA:

#-MÉDIA ABAIXO DE 5.0: REPROVADO
#-MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
#-MÉDIA 7.0 OU SUPERIOR: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))

if media < 5:
    resultado = 'REPROVADO'
elif media >= 5 and media <= 6.9:
    resultado = 'RECUPERAÇÃO'
else:
    resultado = 'APROVADO'

print('O aluno está {}.'.format(resultado))