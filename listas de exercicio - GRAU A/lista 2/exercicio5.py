# 5. Um motorista deseja encher o tanque do seu carro com gasolina. Escreva um algoritmo para ler o
# preço do litro da gasolina e o valor que o motorista tem disponível para abastecer. Calcule quantos
# litros ele conseguiu colocar no tanque e exiba na tela.

preco = float(input('Digite o valor da gasolina: '))
dinheiro = float(input('Digite o valor que você deseja gastar: '))

soma = (dinheiro/preco)

print('O motorista conseguiu abastecer ', soma, 'litros')