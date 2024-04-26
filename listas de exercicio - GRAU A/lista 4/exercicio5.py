  # e. Ler 15 números e escrever a soma e a média dos números lidos.
def main():
    # Inicializando variáveis para soma e contador
    soma = 0
    contador = 0

    # Loop para ler os 15 números
    for i in range(15):
        # Solicitação de entrada do usuário e conversão para float
        numero = float(input(f"Digite o {i+1}º número: "))
        # Adiciona o número à soma
        soma += numero
        # Incrementa o contador
        contador += 1

    # Calcula a média
    media = soma / contador

    # Exibe a soma e a média
    print(f"A soma dos números é: {soma}")
    print(f"A média dos números é: {media}")

# Chama a função principal
if __name__ == "__main__":
    main()