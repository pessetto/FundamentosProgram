# 7. Descubra, dentre cinco nomes informados pelo usuário, qual o primeiro em ordem alfabética.

def encontrar_primeiro_nome():
    # Inicializa uma lista vazia para armazenar os nomes
    nomes = []

    # Solicita ao usuário que insira cinco nomes
    for i in range(5):
        nome = input(f"Digite o {i+1}º nome: ")
        nomes.append(nome)

    # Encontra o primeiro nome em ordem alfabética
    primeiro_nome = min(nomes)

    # Imprime o primeiro nome em ordem alfabética
    print("O primeiro nome em ordem alfabética é:", primeiro_nome)

if __name__ == "__main__":
    encontrar_primeiro_nome()
