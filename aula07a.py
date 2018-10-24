pow(4, 3) #potencia: 4 ao cubo
81**(1/2) #raiz quadrada de 81
81**(1/30) #raiz cubica
'='*20 #repete = vinte vezes

#nome = input('Qual é o seu nome? ')
#print('Prazer em te conhecer {:20}!'.format(nome))
#print('Prazer em te conhecer {:>20}!'.format(nome))
#print('Prazer em te conhecer {:<20}!'.format(nome))
#print('Prazer em te conhecer {:^20}!'.format(nome))
#print('Prazer em te conhecer {:=^20}!'.format(nome))


n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('Soma: {} \nProduto: {} \nDivisão: {:.3f}'.format(s, m, d), end='>>>')
print('\nDivisão inteira: {} \nPotência {}'.format(di, e))
#print('A soma vale {}!'.format(n1+n2))
