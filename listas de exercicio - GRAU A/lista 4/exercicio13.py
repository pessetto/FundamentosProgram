# 6. Crie um algoritmo que sorteie 5 valores entre 0 e 100 e depois imprima o menor, o maior e a média dos valores sorteados.

import random

def main():
    # Inicializa uma lista vazia para armazenar os valores sorteados
    valores = []

    # Sorteia 5 valores entre 0 e 100 e os adiciona à lista
    for _ in range(5):
        valores.append(random.randint(0, 100))

    # Encontra o menor e o maior valor na lista
    menor_valor = min(valores)
    maior_valor = max(valores)

    # Calcula a média dos valores
    media_valores = sum(valores) / len(valores)

    # Imprime os resultados
    print("Valores sorteados:", valores)
    print("Menor valor:", menor_valor)
    print("Maior valor:", maior_valor)
    print("Média dos valores:", media_valores)

if __name__ == "__main__":
    main()