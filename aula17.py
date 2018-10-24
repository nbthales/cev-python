# VARIÁVEIS COMPOSTAS - LISTAS
# () tupla, [] lista, {} dicionario.

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)
lanche.append('cookie')  #cria um elemento na lista
print(lanche)
lanche.insert(0, 'cachorro quente')  #adicionando cq na posicao 0
print(lanche)
del lanche[2]  #eliminando
lanche.pop(4)  #elimina pela posição
lanche.pop()  #elimina o último elemento
lanche.remove('pizza')  #elimina pelo conteudo
print(lanche)

#procurando na lista se tem pizza, se tiver, remove
if 'pizza' in lanche:
    lanche.remove('pizza')

#criando lista através de range
valores = list(range(4, 11))
print(valores)

#ordenando uma lista
valoress = [8, 2, 5, 4, 9, 3, 0]
print(valoress)
valoress.sort()
print(valoress)

valoress.sort(reverse=True)
print(f'{valoress} em ordem inversa')

print(f'{len(valoress)} elementos na lista')

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)  #na posicao 2, inserir o 0
num.pop()  #elimina o último
num.pop(2)  #elimina posicao 2
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')

val = []
val.append(5)
val.append(9)
val.append(4)
print(val)


for v in val:
    print(f'{v}...', end='')

print('\n')

for c, v in enumerate(val):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista.')

# LENDO PELO TECLADO

va = list()

for cont in range(0, 5):
    va.append(int(input('Digite um valor: ')))

for cc, vv in enumerate(va):
    print(f'Na posição {cc} encontrei o valor {vv}')
print('Cheguei no final da lista')


####

a = [2, 3, 4, 7]
#b = a  # cria uma ligação entre as listas
b = a[:]  # b recebe uma cópia dos valores de a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
