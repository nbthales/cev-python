frase = 'Curso em Vídeo Python'
frasespace = '    Curso em vídeo Python    '
print(frase)
print('Splitando a frase {}'.format(frase.split()))
dividindo = frase.split()
print('Mostrando a posição 0 do split: {}'.format(dividindo[0]))
print('Mostrando a 2 letra da posição 0 do split: {}'.format(dividindo[0][1]))
print('A palavra Curso está dentro da frase?: {}'.format('Curso' in frase))
print('Qual posição está o vídeo? {}'.format(frase.find('Vídeo')))
print('Qual posição está o vídeo? {}'.format(frase.lower().find('vídeo')))
print('Trocando palavras: {}'.format(frase.replace('Python', 'Android')))
print('Quantas letras *o* na frase {}'.format(frase.count('o')))
print('Joga a frase pra maiusculo e conta quantos *O* tem: {}'.format(frase.upper().count('O')))
print('Qual o tamanho da frase: {}'.format(len(frase)))
print('Qual o tamanho da frase com espaço {}'.format(len(frasespace)))
print('Removendo espaços antes e depois da frase {}'.format(len(frasespace.strip())))
print('Quarta letra: {}'.format(frase[3]))
print('Quarta letra até a 12: {}'.format(frase[3:13]))
print('Do ínicio até o 12: {}'.format(frase[:13]))
print('4 até 12 pulando de 2 em 2: {}'.format(frase[3:13:2]))
print('4 até o final pulando 2 em 2: {}'.format(frase[3::2]))
print('ínicio ao final pulando 3 em 3: {}'.format(frase[::3]))

print('''Testando um texto
longo
jsdifsafsdof
akdoskfpafpa''')
