#DESAFIO 027

#FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA
#O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE.

#EX: Ana Maria de Souza
#primeiro= Ana
#último= Souza

nome = str(input('Digite seu nome completo: ')).strip().split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
