# 11) Crie um programa para informar quais e quantas notas são necessárias para entregar o mínimo de cédulas para um determinado valor informado pelo usuário considerando notas de R$ 100, R$ 50, R$ 20, R$ 10 e R$ 5 e R$ 1. Seu programa deve mostrar apenas as notas utilizadas. Por exemplo, ao solicitar R$18, o programa deve informar apenas a seguinte informação (note que não foram exibidas informações sobre as demais cédulas):
# 1 nota(s) de R$ 10.
# 1 nota(s) de R$ 5.
# 3 nota(s) de R$ 1.

valor = float(input('Digite o valor a ser sacado: '))
if valor < 1:
    print("o valor digitado não pode ser sacado")

else:
    cem= valor//100
    resto= valor%100

    cinquenta= resto//50
    resto %= 50

    vinte= resto//20
    resto %=20

    dez= resto//10
    resto %=10

    cinco= resto//5
    resto %=5

    um= resto//1

total = ((um*1)+(cinco*5)+(dez*10)+(vinte*20)+(cinquenta*50)+(cem*100))
print("O valor sacado: R$", total)

if cem >= 1:
    print("Notas de R$ 100:", cem)

if cinquenta >= 1:
    print("Notas de R$ 50:", cinquenta)

if vinte >= 1:
    print("Notas de R$ 20:", vinte)

if dez >= 1:
    print("Notas de R$ 10:", dez)

if cinco >= 1:
    print("Notas de R$ 5:", cinco)

if um >= 1:
    print("Notas de R$ 1:", um)