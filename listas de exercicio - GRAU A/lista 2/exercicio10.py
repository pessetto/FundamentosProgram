# 10. O lojista gostou tanto do seu programa anterior que encomendou outro. Dessa vez ele quer que
# você calcule quanto cada cliente gastou na loja apenas informando o número de camisetas, calças
# e cintos comprados. As camisetas custam R$ 25,00, as calças cem reais e os cintos 40 reais. Some o
# valor da compra e ao final dê um desconto de 10 por cento sobre o total. Exiba na tela o valor do
# desconto e o valor da compra.

camiseta = float(25)
calca = float(100)
cinto = float(40)
qtdCamiseta = int(input('Digite a quantidade de CAMISETAS compradas: '))
qtdCalca = int(input('Digite a quantidade de CALÇAS compradas: '))
qtdCinto = int(input('Digite a quantidade de CINTOS compradas: '))

somaCamiseta = (qtdCamiseta*camiseta)
somaCaca = (qtdCalca*calca)
somaCinto = (qtdCinto*cinto)

somaTotal = (somaCinto + somaCinto + somaCaca)
desconto = (somaTotal*0.10)
pago = (somaTotal*0.90)

print('Você obteve R$', desconto, 'de desconto, então pagará R$', pago, 'na sua compra.')