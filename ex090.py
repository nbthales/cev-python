# DESAFIO 090

# FAÇA UM PROGRAMA QUE LEIA NOME E MÉDIA DE UM ALUNO,
# GUARDANDO TAMBÉM A SITUAÇÃO EM UM DICIONÁRIO.
# NO FINAL, MOSTRE O CONTEÚDO DA ESTRUTURA NA TELA.

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')

