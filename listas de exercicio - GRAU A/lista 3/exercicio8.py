# 8) Um comerciante comprou um produto e quer vendê-lo com lucros diferentes dependendo do valor da compra. Ele quer um lucro de 45% se o valor da compra for menor que R$ 20,00, 35% se o preço for de até 50 reais e lucro de 25% se valor for maior. Entrar com o valor do produto e imprimir na tela o valor de venda.

produto = float(input('Digite o valor do produto: '))

if produto < 20:
    soma = produto * 0.45
    somaF = produto + soma
    print('O valor final do produto ficará R$', somaF)

elif produto <= 50:
    soma = produto * 0.35
    somaF = produto + soma
    print('O valor final do produto ficará R$', somaF)

elif produto > 50:
    soma = produto * 0.25
    somaF = produto + soma
    print('O valor final do produto ficará R$', somaF)