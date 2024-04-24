# 1. (2.0 pts) Faça uma função divisivelPor2 que receba como parâmetro um número inteiro, e retorne True se o número é divisível por 2, e False caso contrário.
#--------------------------------------------------------------------------------------------------------------
#RESPOSTA:

def divisivelPor2(numero):
    return numero % 2 == 0

def main():
    num = int(input("Digite um número inteiro: "))
    
    if divisivelPor2(num):
        print(f"O número {num} é divisível por 2.")
    else:
        print(f"O número {num} não é divisível por 2.")

if __name__ == "__main__":
    main()


