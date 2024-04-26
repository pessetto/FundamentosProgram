# 3. Um restaurante de buffet a quilo cobra R$ 40,00 por quilo. Escreva um programa que leia o peso
# do prato do cliente e calcule o valor a ser pago.

valor = float(40)
peso = float(input('Digite o peso do prato do cliente: '))
soma = (valor*peso)

print('O cliente deve pagar R$', soma)