# 10) Dados não precisam ser tão “quadrados”, ou cúbicos para ser mais exato. Faça um programa que simule dados de 4, 6, 8, 10, 12 ou 16 faces (apenas estes valores). Peça para o usuário informar no começo do programa quantas faces quer, para depois fazer o sorteio.

import random
dado = int(input("Digite qual dado você quer sortear: "))


if dado ==4:
    sorteio = random.randint(1,4)
    print(sorteio)

elif dado ==6:
    sorteio = random.randint(1,6)
    print(sorteio)

elif dado ==8:
    sorteio = random.randint(1,8)
    print(sorteio)

elif dado ==10:
    sorteio = random.randint(1,10)
    print(sorteio)

elif dado ==12:
    sorteio = random.randint(1,12)
    print(sorteio)

elif dado ==16:
    sorteio = random.randint(1,16)
    print(sorteio)
