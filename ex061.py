#DESAFIO 061

# REFAÇA O DESAFIO 051, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA
# PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A
# ESTRUTURA WHILE.

print('='*30, '\n{:^30}'.format('10 TERMOS DE UM PA'), '\n'+'='*30)

primeiro = int(input('Primeiro termo: '))
razao = int(input(('Razão: ')))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')