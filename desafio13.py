'''faça um algoritmo que leia o salario de um funcionario e
mostre seu novo salario, com 15% de desconto'''

salario= float(input('Informe o salario?:R$'))

desconto= salario +(salario*15/100)

print ('O salario do funcionario que é {} com desconto de 15% passará a ficar R${:.6}'.format(salario,desconto))

