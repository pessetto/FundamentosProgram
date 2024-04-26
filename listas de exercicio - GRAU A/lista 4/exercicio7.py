  # g. Sortear 20 números inteiros entre -10 e 10 e imprimi-los acompanhados da mensagem “POSITIVO”, “NEGATIVO”, ou “NULO”, conforme o caso. No final, imprimir a quantidade de números positivos e negativos lidos.

import random

def main():
    # Inicializando contadores para números positivos e negativos
    positivos = 0
    negativos = 0

    # Loop para sortear e imprimir os 20 números
    for _ in range(20):
        # Sorteia um número entre -10 e 10
        numero = random.randint(-10, 10)
        
        # Verifica se o número é positivo, negativo ou nulo e atualiza os contadores
        if numero > 0:
            print(f"{numero} - POSITIVO")
            positivos += 1
        elif numero < 0:
            print(f"{numero} - NEGATIVO")
            negativos += 1
        else:
            print(f"{numero} - NULO")

    # Exibe a quantidade de números positivos e negativos
    print(f"\nQuantidade de números positivos: {positivos}")
    print(f"Quantidade de números negativos: {negativos}")

# Chama a função principal
if __name__ == "__main__":
    main()