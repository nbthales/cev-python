#DESAFIO 011
#FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE
#EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA
#PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2m2.

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(larg, alt, larg*alt))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format((larg*alt)/2))
