# 2. Um turista deseja comprar dólares em uma casa de câmbio. Escreva um programa que leia a
# cotação do dólar para real, a quantidade de dólares que o turista deseja comprar, e calcule o valor
# total em reais que ele precisará pagar.

dolar = float(input('Digite a cotação do dólar: '))
quantidade = float(input('Digite quanto em dólar você deseja comprar: '))

conversao = (dolar * quantidade)

print ('Para adquirir', quantidade, 'em dólar, você pagará R$', conversao)