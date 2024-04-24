# 2. (3.0 pts) Agora crie uma função divisivelPorN que receba como parâmetro dois números inteiros e retorne  True se o primeiro é divisível pelo segundo, e False caso contrário. O segundo parâmetro não pode ser zero, então cheque isso dentro da função
#--------------------------------------------------------------------------------------------------------------
#RESPOSTA:

def divisivelPorN(numero, divisor):
    if divisor == 0:
        print("Não é possível efetuar divisão por zero.")
        return False
    elif isinstance(numero, int) and isinstance(divisor, int):
        return numero % divisor == 0
    else:
        raise ValueError("Os parâmetros devem ser números inteiros.")

def main():
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))

    if divisivelPorN(num1, num2):
        print(f"{num1} é divisível por {num2}.")
    else:
        print(f"{num1} não é divisível por {num2}.")

if __name__ == "__main__":
    main()
    