#DESAFIO 024

#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA
#COMEÇA OU NÃO COM O NOME "SANTO".

cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].lower() == 'santo')
