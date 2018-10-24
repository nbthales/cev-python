# VARIÁVEIS COMPOSTAS - TUPLAS
# () tupla, [] lista, {} dicionario.
# TUPLAS SÃO IMUTÁVEIS

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)  # mostra a tupla toda
print(lanche[1])  # mostra a posição 1
print(lanche[-2])  # -1 último, -2 penúltimo...
print(lanche[1:3])  # mostra a posição 1 até a 2
print(lanche[2:])  # mostra o elemento 2 até o final
print(lanche[:2])  # mostra do início até o elemento 1

print(len(lanche))  # mostra quantos elementos tem na tupla

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} que está na posição {cont}')

for pos, comida in enumerate(lanche):  # enumerate da o dado e a posição
    print(f'Eu vou comer {comida} que está na posição {pos}')
print('Comi pra caramba!')

print(lanche)
print(sorted(lanche))  # organizado, em ordem

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b  # concatenar as tuplas
print(c)
print(len(c))  # qual o tamanho dessa tupla
print(c.count(5))  # qnts vezes aparece o 5 na tupla?
print(c.index(8))  # em que posição está o 8?
print(c.index(2, 4))  # em que posição está o 2 a partir da posicao 4?

pessoa = ('Thales', 39, 'M', 84.00)
del(pessoa)  #apagando a variável pessoa
print(pessoa)
