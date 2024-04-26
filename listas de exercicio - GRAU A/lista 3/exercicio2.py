# 2) Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que A + C.

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

if a+b < a+c:
    print("A soma de", a, '+', b, 'É menor que a soma de ', a, '+', c)

else:
    print('Os números digitados não atigem a condição esperada.')