# DESAFIO 097

# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA
# escreva(), QUE RECEBA UM TEXTO QUALQUER COMO
# PARÂMETRO E MOSTRE UMA MENSAGEM COM TAMANHO
# ADAPTÁVEL.

# EX: escreva('Olá, Mundo!')
# saída:
# ~~~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~~~


def escreva(txt):
    print('~' * len(txt))
    print(txt)
    print('~' * len(txt))


frase = input('Digite uma frase: ')
escreva(frase)
