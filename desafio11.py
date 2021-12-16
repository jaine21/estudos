'''faça um programa que leia a largura e a altura de uma
parede em metros, calcule a sua area e a quantidade de tinta
necessaria para pinta-la, sabendo que cada litro de
tinta pinta uma areea de 2m²'''

largura= float(input('Largura da parede:'))
altura= float(input('altura da parede:'))

l= largura*altura

print ('Sua parede tem a dimesão de {}x{} e sua area é de {:.2}'.format(largura,altura,l))

a= l/2
print('para pintar essa parede,voce precisara de {:.2}m²'.format(a))