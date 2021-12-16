'''faça um algoritmo que leia o preço de um produto e
mostre seu novo preço, com 5% de desconto'''

produto = float(input('Informe o valor do produto:'))

desconto= produto-(produto*5/100)

print('O valor do produto com desconto de 5% fica no valor de {}'.format(desconto))