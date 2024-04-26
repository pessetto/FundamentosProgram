# 3. Elabore um programa que lê um número de 1 a 9 e mostra a tabuada de multiplicação do número. Exemplo de tela de saída:
#   Entre com um número: 5
#   5 x 1 = 5
#   5 x 2 = 10
#   ...
#   5 x 10 = 50
#   Calcular outro número (s/n)? n

def tabuada_multiplicacao():
    while True:
        try:
            numero = int(input("Entre com um número de 1 a 9: "))
            if 1 <= numero <= 9:
                for i in range(1, 11):
                    resultado = numero * i
                    print(f"{numero} x {i} = {resultado}")
                continuar = input("Calcular outro número (s/n)? ").strip().lower()
                if continuar != 's':
                    break
            else:
                print("Por favor, digite um número válido de 1 a 9.")
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    tabuada_multiplicacao()
