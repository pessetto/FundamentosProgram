  # f. Ler 10 números inteiros e escrever a quantidade de números pares e a quantidade de números ímpares lidos.
def main():
    # Inicializando contadores para números pares e ímpares
    pares = 0
    impares = 0

    # Loop para ler os 10 números
    for i in range(10):
        # Solicitação de entrada do usuário e conversão para int
        numero = int(input(f"Digite o {i+1}º número: "))
        # Verifica se o número é par ou ímpar e atualiza os contadores
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    # Exibe a quantidade de números pares e ímpares
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")

# Chama a função principal
if __name__ == "__main__":
    main()