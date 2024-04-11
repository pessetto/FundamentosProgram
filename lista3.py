# 1) Escreva um programa que leia dois números e efetue uma divisão, mas somente se o divisor for diferente de zero; quando isto ocorrer, é mostrada uma mensagem de erro apropriada.

# numero1 = int(input('Digite um número para dividir: '))
# numero2 = int(input('Digite o número que irá dividir: '))

# if numero2 != 0:
#     soma = numero1/numero2
#     print('O resultado da divisão é: ', soma)

# else:
#     print('O número divisor não pode ser 0')

#-------------------------------------------------------------------------------------------------------------------#

# 2) Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que A + C.

# a = int(input('Digite o primeiro valor: '))
# b = int(input('Digite o segundo valor: '))
# c = int(input('Digite o terceiro valor: '))

# if a+b < a+c:
#     print("A soma de", a, '+', b, 'É menor que a soma de ', a, '+', c)

# else:
#     print('Os números digitados não atigem a condição esperada.')

#-------------------------------------------------------------------------------------------------------------------#

# 3) Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.

# numero = float(input('Digite um número: '))

# if numero >= 0:
#     dobro = numero*2
#     print("O dobro do número digitado é ", dobro)

# else:
#     triplo = numero*3
#     print("O triplo do número digitado é", triplo)

#-------------------------------------------------------------------------------------------------------------------#

# 4) Crie um programa que verifica se um número inteiro informado pelo usuário é divisível por 3.

# numero = int(input('Digite um número inteiro: '))

# if (numero % 3) == 0:
#     print("O número digitado é divisível por 3.")

# else:
#     print("O número digitado NÃO É divisível por 3.")

#-------------------------------------------------------------------------------------------------------------------#

# 5) Faça um algoritmo para receber um número qualquer do usuário e informar na tela se é par ou se é ímpar.

# numero = int(input('Digite um número: '))

# if (numero % 2) == 0:
#     print('O valor digitado é par.')

# else:
#     print('O valor digitado é ímpar.')

#-------------------------------------------------------------------------------------------------------------------#

# 6) Brincadeira do PAR ou ÍMPAR. Pergunte para o usuário se ele aposta em PAR ou ÍMPAR. Depois disso, peça para ele digitar um número de 0 a 5 (como se fosse mostrar os dedos da mão. Sorteie um número de 0 a 5 e some com o que o usuário digitou. Se o usuário escolheu PAR e o valor da soma for par OU se ele escolheu ÍMPAR e o valor da soma é ímpar, diga que ele venceu. Senão, diga que o programa venceu

# import random
# usuario = input("Digite P para escolher par e I para impar: ")
# numeroU = int(input('Digite um número de 0 a 5: '))

# sorteio = random.randint(1,5)
# print('Numero sorteado pela máquina: ', sorteio)

# if usuario == 'P' and ((numeroU + sorteio)%2)==0:
#     print('Você ganhou!')

# elif usuario == 'I' and ((numeroU + sorteio)%3)==0:
#     print('Você ganhou!')

# else:
#     print('O programa ganhou, tente novamente :(')

#-------------------------------------------------------------------------------------------------------------------#

# 7) Implementar um programa que calcula o desconto previdenciário de um funcionário. O programa deve, dado um salário retornar o valor do desconto proporcional ao mesmo. O cálculo de desconto segue a regra: o desconto deve 11% do valor do salário. Entretanto, o valor máximo de desconto é 318,20. Sendo assim, ou o método retorna 11% sobre o salário ou 318,20.

# salario = float(input('Digite o seu salário: '))

# desconto = (salario * 0.11)
# # salarioF = (salario * 0.89)

# if desconto > 318.20:
#     print('O desconto foi de R$318.20')

# else:
#     print('O desconto do seu salário foi de R$', desconto)

#-------------------------------------------------------------------------------------------------------------------#

# 8) Um comerciante comprou um produto e quer vendê-lo com lucros diferentes dependendo do valor da compra. Ele quer um lucro de 45% se o valor da compra for menor que R$ 20,00, 35% se o preço for de até 50 reais e lucro de 25% se valor for maior. Entrar com o valor do produto e imprimir na tela o valor de venda.

# produto = float(input('Digite o valor do produto: '))

# if produto < 20:
#     soma = produto * 0.45
#     somaF = produto + soma
#     print('O valor final do produto ficará R$', somaF)

# elif produto <= 50:
#     soma = produto * 0.35
#     somaF = produto + soma
#     print('O valor final do produto ficará R$', somaF)

# elif produto > 50:
#     soma = produto * 0.25
#     somaF = produto + soma
#     print('O valor final do produto ficará R$', somaF)

#-------------------------------------------------------------------------------------------------------------------#

# !!!!!!!!!! NÃO ESTÁ FUNCIONANDO !!!!!!!!!!!!!!!!!!
# 9) Faça um conversor de câmbio de reais/dólar/euro. O usuário deve informar inicialmente a cotação de cada moeda em relação ao real. Depois apresente o seguinte menu:
# 1) Converter de Real para Euro
# 2) Converter de Real para Dólar
# 3) Converter de Euro para Dólar
# 4) Converter de Euro para Real
# 5) Converter de Dólar para Euro
# 6) Converter de Dólar para Real
# Leia o valor a ser convertido na moeda de origem e imprima na tela a quantidade na moeda destino.

# realEuro = float(input("insira a cotacao do Real para o Euro: "))
# realDolar = float(input("insira a cotacao do Real para o Dolar: "))
# euroDolar = float(input("insira a cotacao do Euro para o Dolar: "))

# print("Menu:")
# print("1) Converter de Real para Euro")
# print("2) Converter de Real para Dólar")
# print("3) Converter de Euro para Dólar")
# print("4) Converter de Euro para Real")
# print("5) Converter de Dólar para Euro")
# print("6) Converter de Dólar para Real")

# opcao = int(input("escolha uma opcao: "))

# if opcao == 1:
#         valor = float(input("insira o valor em Reais: "))
#         conversao = valor * realEuro
#         print(f"valor em Euro: {conversao}")
        
# elif opcao == 2:
#         valor = float(input("insira o valor em Reais: "))
#         conversao = valor * realDolar
#         print(f"valor em Dólar: {conversao}")
        
# elif opcao == 3:
#         valor = float(input("insira o valor em Euro: "))
#         conversao = valor * euroDolar
#         print(f"valor em Dólar: {conversao}")
        
# elif opcao == 4:
#         valor = float(input("insira o valor em Euro: "))
#         conversao = valor / realEuro
#         print(f"valor em Reais: {conversao}")
        
# elif opcao == 5:
#         valor = float(input("insira o valor em Dólar: "))
#         conversao = valor / euroDolar
#         print(f"valor em Euro: {conversao}")
        
# elif opcao == 6:
#         valor = float(input("insira o valor em Dólar: "))
#         conversao = valor / realDolar
#         print(f"valor em Reais: {conversao}")
        
# else:
#         print("erro") 

#-------------------------------------------------------------------------------------------------------------------#

# 10) Dados não precisam ser tão “quadrados”, ou cúbicos para ser mais exato. Faça um programa que simule dados de 4, 6, 8, 10, 12 ou 16 faces (apenas estes valores). Peça para o usuário informar no começo do programa quantas faces quer, para depois fazer o sorteio.

# import random
# dado = int(input("Digite qual dado você quer sortear: "))


# if dado ==4:
#     sorteio = random.randint(1,4)
#     print(sorteio)

# elif dado ==6:
#     sorteio = random.randint(1,6)
#     print(sorteio)

# elif dado ==8:
#     sorteio = random.randint(1,8)
#     print(sorteio)

# elif dado ==10:
#     sorteio = random.randint(1,10)
#     print(sorteio)

# elif dado ==12:
#     sorteio = random.randint(1,12)
#     print(sorteio)

# elif dado ==16:
#     sorteio = random.randint(1,16)
#     print(sorteio)

#-------------------------------------------------------------------------------------------------------------------#

# 11) Crie um programa para informar quais e quantas notas são necessárias para entregar o mínimo de cédulas para um determinado valor informado pelo usuário considerando notas de R$ 100, R$ 50, R$ 20, R$ 10 e R$ 5 e R$ 1. Seu programa deve mostrar apenas as notas utilizadas. Por exemplo, ao solicitar R$18, o programa deve informar apenas a seguinte informação (note que não foram exibidas informações sobre as demais cédulas):
# 1 nota(s) de R$ 10.
# 1 nota(s) de R$ 5.
# 3 nota(s) de R$ 1.

# valor = float(input('Digite o valor a ser sacado: '))
# if valor < 1:
#     print("o valor digitado não pode ser sacado")

# else:
#     cem= valor//100
#     resto= valor%100

#     cinquenta= resto//50
#     resto %= 50

#     vinte= resto//20
#     resto %=20

#     dez= resto//10
#     resto %=10

#     cinco= resto//5
#     resto %=5

#     um= resto//1

# total = ((um*1)+(cinco*5)+(dez*10)+(vinte*20)+(cinquenta*50)+(cem*100))
# print("O valor sacado: R$", total)

# if cem >= 1:
#     print("Notas de R$ 100:", cem)

# if cinquenta >= 1:
#     print("Notas de R$ 50:", cinquenta)

# if vinte >= 1:
#     print("Notas de R$ 20:", vinte)

# if dez >= 1:
#     print("Notas de R$ 10:", dez)

# if cinco >= 1:
#     print("Notas de R$ 5:", cinco)

# if um >= 1:
#     print("Notas de R$ 1:", um)

#-------------------------------------------------------------------------------------------------------------------#

# 12) A confederação brasileira de natação irá promover eliminatórias para o próximo mundial. Fazer um algoritmo que receba a idade de um nadador e imprima a sua categoria segundo a tabela a seguir:
# Categoria Idade
# Infantil A 5-7 anos
# Infantil B 8-10 anos
# Juvenil A 11-13 anos
# Juvenil B 14-17 anos
# Sênior Maiores de 18 anos
        
# grauA = float(input("insira a nota do grau A: "))
# grauB = float(input("insira a nota do grau B: "))
# mediaFinal = ((grauA + grauB*2)/3)

# print(f"a média final será: {format(mediaFinal, '.2f')}")

# if mediaFinal >= 6:
#     print("o aluno passou por media")
# else:
#     print("o aluno ficou em recuperacao")
#     grauC = float(input("insira a nota do grau C: "))
#     substituir = input("substituir a nota do grau A (A) ou do grau B (B)? ").upper()
    
#     if substituir == "A":
#         mediaFinal = ((grauC + grauB*2)/3)
#     elif substituir == "B":
#         mediaFinal = ((grauA + grauC*2)/3)
#     else: 
#         print("erro")
        
#     if mediaFinal >= 6:
#         print("media o aluno foi aprovado com média", format(mediaFinal, '.2f'))
#     else:
#         print("o aluno foi reprovado com média", format(mediaFinal, '.2f'))

#-------------------------------------------------------------------------------------------------------------------#

# 13) Faça um programa que leia a nota do Grau A e do Grau B do aluno e calcule a média final conforme as regras da Unisinos. Imprima a média final na tela e diga se o aluno passou por média ou se ficou em recuperação (grau C). Se o aluno ficou em recuperação, pergunte se ele quer substituir o Grau A ou o Grau B (ele deve digitar ‘a’ ou ‘b’). Leia a nota do Grau C, recalcule a média de acordo com o grau substituído e imprima na tela o resultado, informando se ele foi aprovado ou reprovado.
        
# valorAdicional = 0

# idadeConveniado = int(input("insira a idade do conveniado: "))
# qtdDependentes = int(input("insira a quantidade de dependentes: "))

# if idadeConveniado < 10:
#     valorAdicional += 100
    
# elif 10 <= idadeConveniado <= 30:
#     valorAdicional += 220
    
# elif 31 <= idadeConveniado <= 60:
#     valorAdicional += 395
    
# else:
#     valorAdicional += 480

# for i in range(qtdDependentes):
#     idadeDependente = int(input(f"insira a idade do dependente {i + 1}: "))
    
#     if idadeDependente < 10:
#         valorAdicional += 100
        
#     elif 10 <= idadeDependente <= 30:
#         valorAdicional += 220
        
#     elif 31 <= idadeDependente <= 60:
#         valorAdicional += 395
        
#     else:
#         valorAdicional += 480

# valorTotal = 300 + (valorAdicional * qtdDependentes)

# print(f"o valor do plano de saúde sera: R${valorTotal:.2f}")

#-------------------------------------------------------------------------------------------------------------------#

# 14) Criar um programa para identificar o valor a ser pago por um plano de saúde dada a idade do conveniado considerando que todos pagam R$ 300 e mais um adicional (se tiver dependentes) conforme a seguinte tabela:
# a) crianças com menos de 10 anos pagam R$100;
# b) dependentes com idade entre 10 e 30 anos pagam R$220;
# c) dependentes com idade entre 31 e 60 anos pagam R$ 395; 
# d) dependentes com mais de 60 anos pagam R$ 480
        
# precoProduto = float(input("insira o preco do produto: "))

# print("Formas de pagamento:")
# print("1 - à vista em dinheiro")
# print("2 - à vista no cartão de crédito")
# print("3 - em duas vezes")
# print("4 - em três vezes")

# pagamento = int(input("escolha uma opcao: "))

# if pagamento == 1:
#     valorFinal = precoProduto * 0.85  
    
# elif pagamento == 2:
#     valorFinal = precoProduto * 0.90  
    
# elif pagamento == 3:
#     valorFinal = precoProduto  
    
# elif pagamento == 4:
#     valorFinal = precoProduto * 1.10  
    
# else:
#     valorFinal = "erro"

# print(f"O valor a ser pago pelo produto é: R${valorFinal:.2f}")
