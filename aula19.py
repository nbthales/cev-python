# AULA 19 - VARIÁVEIS COMPOSTAS (DICIONÁRIOS)
'''
dados = dict()
dados = {'nome': 'Thales', 'idade': 23}
dados['sexo'] = 'M'
del dados['idade']
print(dados[nome])

filme = {'titulo': 'Star Wars',
         'ano': 1997,
         'diretor': 'George Lucas'
}

print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')
'''

pessoas = {'nome': 'Thales', 'sexo':'M', 'idade': 23}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
#del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('\n\n')

# CRIANDO DICIONARIO DENTRO DE UMA LISTA
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print('\n\n')

estad = dict()
brasi = list()
for c in range(0, 3):
    estad['uf'] = str(input('Unidade Federativa: '))
    estad['sigla'] = str(input('Sigla do Estado: '))
    brasi.append(estad.copy())
for e in brasi:
    #for k, v in e.items():
    #   print(f'O Campo {k} tem valor {v}')
    for v in e.values():
        print(v, end=' ')
    print()
