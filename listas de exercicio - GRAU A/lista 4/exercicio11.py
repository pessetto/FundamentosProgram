# 4. Escrever um programa que calcule todos os números divisíveis por certo valor indicado pelo usuário (o resto da divisão por este número deve ser igual a zero), compreendidos em um intervalo também
# especificado pelo usuário. O usuário deve entrar com um primeiro valor correspondente ao divisor e após ele vai fornecer o valor inicial do intervalo, seguido do valor final deste intervalo. Exemplo de tela de saída:
# Entre com o valor do divisor: 3 
# Início do intervalo: 17
# Final do intervalo: 29
# Números divisíveis por 3 no intervalo de 17 a 29:
# 18 21 24 27

def numeros_divisiveis():
    try:
        divisor = int(input("Entre com o valor do divisor: "))
        inicio_intervalo = int(input("Início do intervalo: "))
        final_intervalo = int(input("Final do intervalo: "))

        print(f"Números divisíveis por {divisor} no intervalo de {inicio_intervalo} a {final_intervalo}:")
        for numero in range(inicio_intervalo, final_intervalo + 1):
            if numero % divisor == 0:
                print(numero, end=" ")
        print()  # Imprime uma linha em branco para melhor legibilidade

    except ValueError:
        print("Por favor, entre com valores inteiros válidos.")

if __name__ == "__main__":
    numeros_divisiveis()