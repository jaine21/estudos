''' crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dolares ela pode comprar

considere US$1.00=R$3,27'''

real = float (input('Informe o valor da sua carteira:R$'))

dol = real / 5.68

print(' Atualmente esse é seu valor em US$ {:.2f}'.format (dol))