# DESAFIO 073

# CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS
# COLOCADOS TA TABELA DO CAMPEONATO BRASILEIRO
# DE FUTEBOL, NA ORDEM DE COLOCAÇÃO. DEPOIS
# MOSTRE:

# A) APENAS OS 5 PRIMEIROS COLOCADOS.
# B) OS ÚLTIMOS 4 COLOCADOS DA TABELA.
# C) UMA LISTA COM OS TIMES EM ORDEM ALFABÉTICA.
# D) EM QUE POSIÇÃO NA TABELA ESTÁ O TIME DA
#    CHAPECOENSE.

times = ('Palmeiras', 'Internacional', 'Flamengo', 'Grêmio',
         'São Paulo', 'Atlético-MG', 'Santos', 'Atlético-PR',
         'Fluminense', 'Bahia', 'Cruzeiro', 'Corinthians',
         'Botafogo', 'Vasco', 'América-MG', 'Vitória', 'Ceará',
         'Chapecoense', 'Sport', 'Paraná')

print('-='*20)
print(f'Lista de times do Brasileirão: {times}')
print('-='*20)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*20)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*20)
chape = times.index('Chapecoense')
print(f'O Chapecoense está na {chape+1} posição')
print('-='*20)
