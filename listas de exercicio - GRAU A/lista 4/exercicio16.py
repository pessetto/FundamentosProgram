# 9. Escrever um programa que produza a saída abaixo na tela, para n linhas e usando um caractere lido do teclado.
# Exemplo de tela de saída, para n = 5 e caracter = `*`:
# Entre com um número: 5
# Entre com um caracter: *
# *
# * *
# * * *
# * * * *
# * * * * *

def imprimir_padrao(n, caractere):
    for i in range(1, n + 1):
        print(caractere * i)

def main():
    try:
        n = int(input("Entre com um número: "))
        caractere = input("Entre com um caractere: ")

        imprimir_padrao(n, caractere)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()