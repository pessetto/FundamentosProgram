  # h. Ler n números e imprimir no final a soma dos números lidos (obs.: n é a quantidade de números que deverão ser lidos e também deve ser lido do teclado)

def main():
    # Solicitação da quantidade de números a serem lidos
    n = int(input("Digite a quantidade de números a serem lidos: "))

    # Inicializando variável para a soma
    soma = 0

    # Loop para ler os 'n' números
    for i in range(n):
        # Solicitação de entrada do usuário e conversão para int
        numero = float(input(f"Digite o {i+1}º número: "))
        # Adiciona o número à soma
        soma += numero

    # Exibe a soma dos números lidos
    print(f"A soma dos números é: {soma}")

# Chama a função principal
if __name__ == "__main__":
    main()