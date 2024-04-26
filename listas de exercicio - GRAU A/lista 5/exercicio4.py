# 4. Implemente uma função sorteio que receba o intervalo de valores inteiros início e fim como parâmetro e sorteie um número dentro do intervalo (considerando intervalo fechado [início, fim])

import random

def sorteio(inicio, fim):
    # Sorteia um número inteiro dentro do intervalo [inicio, fim]
    numero_sorteado = random.randint(inicio, fim)
    return numero_sorteado

# Exemplo de uso da função sorteio
inicio_intervalo = int(input("Digite o início do intervalo: "))
fim_intervalo = int(input("Digite o fim do intervalo: "))
numero_sorteado = sorteio(inicio_intervalo, fim_intervalo)
print("Número sorteado:", numero_sorteado)