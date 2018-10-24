# DESAFIO 071

# CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA
# ELETRÔNICO. NO INÍCIO, PERGUNTE AO USUÁRIO QUAL SERÁ O
# VALOR A SER SACADO (NÚMERO INTEIRO) E O PROGRAMA VAI INFORMAR
# QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES.

# OBS: CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE R$50, R$20,
# R$10 E R$1.

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! TENHA UM BOM DIA!')