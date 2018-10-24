#DESAFIO 057

#FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA,
#MAS SÓ ACEITE OS VALORES 'M' OU 'F'.
#CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE
#ATÉ TER UM VALOR CORRETO

sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido, digite novamente: ')).strip().upper()[0]
print('Sexo {} registrado com SUCESSO!'.format(sexo))
