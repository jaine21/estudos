'''escreva um programa que leia um valor em metros e o exiba
convertido em centimetros e milimetros'''

a = int(input('Informe o valor para conversão em centimetro e milimetro: '))

b = a * 100
c = a * 1000

print ('{} refere-se a centimetro e {}, a milimetros'.format(b, c, a))