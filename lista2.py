# 1. Faça um algoritmo que leia uma quantidade de tempo em minutos e escreva o tempo equivalente
# em segundos na tela.

# minutos = int(input('Digite o tempo em minutos: '))
# segundos = minutos * 60

# print(minutos, 'mitutos, equivalem a', segundos, 'segundos')

# ___________________________________________________________________________________________________
# 2. Um turista deseja comprar dólares em uma casa de câmbio. Escreva um programa que leia a
# cotação do dólar para real, a quantidade de dólares que o turista deseja comprar, e calcule o valor
# total em reais que ele precisará pagar.

# dolar = float(input('Digite a cotação do dólar: '))
# quantidade = float(input('Digite quanto em dólar você deseja comprar: '))

# conversao = (dolar * quantidade)

# print ('Para adquirir', quantidade, 'em dólar, você pagará R$', conversao)

# ____________________________________________________________________________________________________
# 3. Um restaurante de buffet a quilo cobra R$ 40,00 por quilo. Escreva um programa que leia o peso
# do prato do cliente e calcule o valor a ser pago.

# valor = float(40)
# peso = float(input('Digite o peso do prato do cliente: '))
# soma = (valor*peso)

# print('O cliente deve pagar R$', soma)

# ____________________________________________________________________________________________________
# 4. Faça um algoritmo que permita ao aluno calcular a sua média final na Unisinos. Leia a nota do grau
# A e do grau B e escreva o resultado na tela. Lembrando que o Grau A vale 1/3 e o Grau B 2/3.

# grauA = float(input('Digite sua nota do Grau A: '))
# grauB = float(input('Digite sua nota do Grau B: '))
# soma = (((grauA*1)+(grauB*2))/3)
# print(soma)


# ____________________________________________________________________________________________________
# 5. Um motorista deseja encher o tanque do seu carro com gasolina. Escreva um algoritmo para ler o
# preço do litro da gasolina e o valor que o motorista tem disponível para abastecer. Calcule quantos
# litros ele conseguiu colocar no tanque e exiba na tela.

# preco = float(input('Digite o valor da gasolina: '))
# dinheiro = float(input('Digite o valor que você deseja gastar: '))

# soma = (dinheiro/preco)

# print('O motorista conseguiu abastecer ', soma, 'litros')

# ____________________________________________________________________________________________________
# 6. A loja de eletrônicos TechMundo vende uma certa quantidade de smartphones e uma quantidade
# de tablets a cada dia. Cada smartphone custa R$ 1000,00 e cada tablet custa R$ 1500,00. Ao final
# do dia, o dono quer saber quanto arrecadou com a venda dos smartphones e dos tablets. Escreva
# um programa que leia o número de smartphones e tablets vendidos em um dia e calcule o total
# arrecadado.

# valorCelular = float(1000)
# valorTablet = float(1500)
# quantidadeCelular = int(input('Quantos celulares foram vendidos hoje? '))
# quantidadeTablet = int(input('Quantos Tablets foram vendidos hoje? '))

# soma = ((quantidadeCelular*valorCelular) + (quantidadeTablet*valorTablet))

# print('Foram vendidos ', quantidadeCelular, 'celulares e ', quantidadeTablet, 'tablets. O lucro total de hoje foi de R$',soma)

# ____________________________________________________________________________________________________
# 7. Um criador de pássaros deseja saber a quantidade de ração diária necessária para alimentar seus
# pássaros. Cada pássaro consome 30 gramas de ração por dia. Escreva um programa que leia o
# número de pássaros que o criador possui e calcule a quantidade total de ração necessária por dia.

# racao = float(0.30)
# passaros = int(input('Digite quantos pássaros serão alimentados: '))

# soma = (passaros*racao)

# print(soma)

# ____________________________________________________________________________________________________
# 8. Um usuário deseja converter a temperatura de Celsius para Fahrenheit. Escreva um programa que
# leia a temperatura em Celsius e exiba a temperatura equivalente em Fahrenheit.

# graus = int(input('Qual a temperatura em graus você deseja converter: '))
# soma = ((graus * 9/5) + 32)

# print(soma)

# ____________________________________________________________________________________________________
# 9. Durante uma liquidação uma loja resolveu dar quinze por cento de desconto nas compras feitas
# pelos clientes. Faça um programa que leia o valor da compra e escreva o valor da compra com o
# desconto.

# compra = float(input('Digite o valor da compra do cliente: '))
# soma = (compra*0.85)

# print('O valor da sua compra com 15% de desconto ficou:', soma)

# ____________________________________________________________________________________________________
# 10. O lojista gostou tanto do seu programa anterior que encomendou outro. Dessa vez ele quer que
# você calcule quanto cada cliente gastou na loja apenas informando o número de camisetas, calças
# e cintos comprados. As camisetas custam R$ 25,00, as calças cem reais e os cintos 40 reais. Some o
# valor da compra e ao final dê um desconto de 10 por cento sobre o total. Exiba na tela o valor do
# desconto e o valor da compra.

# camiseta = float(25)
# calca = float(100)
# cinto = float(40)
# qtdCamiseta = int(input('Digite a quantidade de CAMISETAS compradas: '))
# qtdCalca = int(input('Digite a quantidade de CALÇAS compradas: '))
# qtdCinto = int(input('Digite a quantidade de CINTOS compradas: '))

# somaCamiseta = (qtdCamiseta*camiseta)
# somaCaca = (qtdCalca*calca)
# somaCinto = (qtdCinto*cinto)

# somaTotal = (somaCinto + somaCinto + somaCaca)
# desconto = (somaTotal*0.10)
# pago = (somaTotal*0.90)

# print('Você obteve R$', desconto, 'de desconto, então pagará R$', pago, 'na sua compra.')
