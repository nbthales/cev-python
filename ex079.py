# DESAFIO 079

# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS
# VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA. CASO O
# NÚMERO JÁ EXISTA LÁ DENTRO, ELE NÃO SERÁ ADICIONADO.

# NO FINAL, SERÃO EXIBIDOS OS OS VALORES ÚNICOS DIGITADOS
# EM ORDEM CRESCENTE

numeros = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar....')
    op = str(input(('Quer continuar? [S/N] '))).lower()
    if op == 'n':
        break
print('-=' * 30)
numeros.sort()
print(f'Valores digitados: {numeros}')
