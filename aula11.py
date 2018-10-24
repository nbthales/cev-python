# CORES NO TERMINAL PADRÃO ANSI (ESCAPE SEQUENCE)

# [STYLE; TEXT; BACK]
# STYLE 0 Nenhum; 1 negrito; 4 sublinhado; 7 invertido
# TEXT(CORES) 30 branco; 31 vermelho; 32 verde; 33 amarelo; 34 azul; 35 lilas; 36 cyan e 37 cinza
# BACK(FUNDO) 40 branco; 41 vermelho; 42 verde; 43 amarelo; 44 azul; 45 lilas; 46 cyan e 47 cinza

print('\033[1mNegrito')
print('\033[4mSublinhado')
print('\033[7mInvertido\033[m')

print('\033[0;30mBranco')
print('\033[0;31mVermelho')
print('\033[0;32mVerde')
print('\033[0;33mAmarelo')
print('\033[0;34mAzul')
print('\033[0;35mLilas')
print('\033[0;36mCyan')
print('\033[0;37mCinza')

print('\033[0;;40mFundo Branco\033[m')
print('\033[0;;41mFundo Vermelho\033[m')
print('\033[0;;42mFundo Verde\033[m')
print('\033[0;;43mFundo Amarelo\033[m')
print('\033[0;;44mFundo Azul\033[m')
print('\033[0;;45mFundo Lilas\033[m')
print('\033[0;;46mFundo Cyan\033[m')
print('\033[0;;47mFundo Cinza\033[m')

a = 3;
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m.'.format(a, b))

nome = 'Thales'
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'azul': '\033[34m'}

print('Olá {}{}{}! Prazer em te conhecer!'.format(cores['vermelho'], nome, cores['limpa']))
