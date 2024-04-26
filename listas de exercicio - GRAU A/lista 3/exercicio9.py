# 9) Faça um conversor de câmbio de reais/dólar/euro. O usuário deve informar inicialmente a cotação de cada moeda em relação ao real. Depois apresente o seguinte menu:
# 1) Converter de Real para Euro
# 2) Converter de Real para Dólar
# 3) Converter de Euro para Dólar
# 4) Converter de Euro para Real
# 5) Converter de Dólar para Euro
# 6) Converter de Dólar para Real
# Leia o valor a ser convertido na moeda de origem e imprima na tela a quantidade na moeda destino.

realEuro = float(input("insira a cotacao do Real para o Euro: "))
realDolar = float(input("insira a cotacao do Real para o Dolar: "))
euroDolar = float(input("insira a cotacao do Euro para o Dolar: "))

print("Menu:")
print("1) Converter de Real para Euro")
print("2) Converter de Real para Dólar")
print("3) Converter de Euro para Dólar")
print("4) Converter de Euro para Real")
print("5) Converter de Dólar para Euro")
print("6) Converter de Dólar para Real")

opcao = int(input("escolha uma opcao: "))

if opcao == 1:
        valor = float(input("insira o valor em Reais: "))
        conversao = valor * realEuro
        print(f"valor em Euro: {conversao}")
        
elif opcao == 2:
        valor = float(input("insira o valor em Reais: "))
        conversao = valor * realDolar
        print(f"valor em Dólar: {conversao}")
        
elif opcao == 3:
        valor = float(input("insira o valor em Euro: "))
        conversao = valor * euroDolar
        print(f"valor em Dólar: {conversao}")
        
elif opcao == 4:
        valor = float(input("insira o valor em Euro: "))
        conversao = valor / realEuro
        print(f"valor em Reais: {conversao}")
        
elif opcao == 5:
        valor = float(input("insira o valor em Dólar: "))
        conversao = valor / euroDolar
        print(f"valor em Euro: {conversao}")
        
elif opcao == 6:
        valor = float(input("insira o valor em Dólar: "))
        conversao = valor / realDolar
        print(f"valor em Reais: {conversao}")
        
else:
        print("erro") 
