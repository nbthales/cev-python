# DESAFIO 096

# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA
# área(), QUE RECEBA AS DIMENSÕES DE UM TERRENO
# RETANGULAR (LARGURA E COMPRIMENTO) E MOSTRE
# A ÁREA DO TERRENO.


def area(l, c):
    s = l * c
    print(f'A Área de um terreno {l}x{c} é de {s:.1f}m².')


print('Controle de Terrenos\n' + '-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
