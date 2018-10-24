#DESAFIO 062

# MELHORE O DESAFIO 061, PERGUNTANDO PARA O USUÁRIO SE ELE QUER
# MOSTRAR MAIS ALGUNS TERMOS. O PROGRAMA ENCERRA QUANDO ELE
# DISSER QUE QUER MOSTRAR 0 TERMOS.

print('='*30, '\n{:^30}'.format('10 TERMOS DE UM PA'), '\n'+'='*30)

primeiro = int(input('Primeiro termo: '))
razao = int(input(('Razão: ')))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
