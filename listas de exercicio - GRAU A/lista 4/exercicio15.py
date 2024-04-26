# 8. Fazer um programa que calcule e imprima o fatorial de um número fornecido pelo usuário. Repetir a execução do programa tantas até o usuário responder não. O fatorial de um número inteiro positivo é
# definido como o número multiplicado por ele menos 1, menos 2, etc até o valor 1. Por exemplo, o fatorial de 4 é 4x3x2x1=24. Exemplo de tela de saída:
# Entre com um número: 5
# O fatorial de 5 é 120
# Calcular outro número (s/n)? n

def calcular_fatorial(numero):
    # Caso especial: fatorial de 0 é 1
    if numero == 0:
        return 1
    else:
        # Inicializa o fatorial como 1
        fatorial = 1
        # Calcula o fatorial multiplicando o número por todos os inteiros de 1 até o número
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

def main():
    while True:
        try:
            numero = int(input("Entre com um número: "))
            fatorial = calcular_fatorial(numero)
            print(f"O fatorial de {numero} é {fatorial}")

            calcular_outro = input("Calcular outro número (s/n)? ").strip().lower()
            if calcular_outro != 's':
                break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()