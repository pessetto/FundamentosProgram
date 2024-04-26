# 6. A loja de eletrônicos TechMundo vende uma certa quantidade de smartphones e uma quantidade
# de tablets a cada dia. Cada smartphone custa R$ 1000,00 e cada tablet custa R$ 1500,00. Ao final
# do dia, o dono quer saber quanto arrecadou com a venda dos smartphones e dos tablets. Escreva
# um programa que leia o número de smartphones e tablets vendidos em um dia e calcule o total
# arrecadado.

valorCelular = float(1000)
valorTablet = float(1500)
quantidadeCelular = int(input('Quantos celulares foram vendidos hoje? '))
quantidadeTablet = int(input('Quantos Tablets foram vendidos hoje? '))

soma = ((quantidadeCelular*valorCelular) + (quantidadeTablet*valorTablet))

print('Foram vendidos ', quantidadeCelular, 'celulares e ', quantidadeTablet, 'tablets. O lucro total de hoje foi de R$',soma)
