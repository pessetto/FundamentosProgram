# 2. Implemente um programa que sorteia um número de 1 a 10 e dá ao usuário 3 tentativas de acertá-lo. A cada tentativa errada, o programa informa se o número a adivinhar está abaixo ou acima.

import random

def main():
    # Sorteia um número aleatório de 1 a 10
    numero_secreto = random.randint(1, 10)
    tentativas_restantes = 3

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar um número de 1 a 10.")

    while tentativas_restantes > 0:
        try:
            # Solicita ao usuário um palpite
            palpite = int(input("Digite seu palpite: "))

            # Verifica se o palpite está correto
            if palpite == numero_secreto:
                print("Parabéns! Você acertou o número!")
                break
            elif palpite < numero_secreto:
                print("O número a adivinhar está acima do seu palpite.")
            else:
                print("O número a adivinhar está abaixo do seu palpite.")

            tentativas_restantes -= 1
            print(f"Tentativas restantes: {tentativas_restantes}")

        except ValueError:
            print("Por favor, digite um número válido.")

    if tentativas_restantes == 0:
        print(f"Suas tentativas acabaram. O número correto era {numero_secreto}.")

if __name__ == "__main__":
    main()