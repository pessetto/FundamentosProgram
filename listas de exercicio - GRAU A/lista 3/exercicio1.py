# 1) Escreva um programa que leia dois números e efetue uma divisão, mas somente se o divisor for diferente de zero; quando isto ocorrer, é mostrada uma mensagem de erro apropriada.

numero1 = int(input('Digite um número para dividir: '))
numero2 = int(input('Digite o número que irá dividir: '))

if numero2 != 0:
    soma = numero1/numero2
    print('O resultado da divisão é: ', soma)

else:
    print('O número divisor não pode ser 0')