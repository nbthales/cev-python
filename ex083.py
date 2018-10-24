# DESAFIO 083

# CRIE UM PROGRAMA ONDE O USUÁRIO DIGITE UMA EXPRESSÃO
# QUALQUER QUE USE PARÊNTESES. SEU APLICATIVO DEVERÁ
# ANALISAR SE A EXPRESSÃO PASSADA ESTÁ COM OS PARÊNTESES
# ABERTOS E FECHADOS NA ORDEM CORRETA.

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
