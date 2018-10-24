# DESAFIO 080

# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR CINCO
# VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA, JÁ NA
# POSIÇÃO CORRETA DE INSERÇÃO (SEM USAR O SORT()).

# NO FINAL, MOSTRE A LISTA ORDENADA NA TELA.

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
