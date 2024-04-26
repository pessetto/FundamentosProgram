# 2. Implemente uma função tabuada que receba como parâmetro um número inteiro e escreva a tabuada desse número.

def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Exemplo de uso da função tabuada
num = int(input("Digite um número inteiro: "))
tabuada(num)