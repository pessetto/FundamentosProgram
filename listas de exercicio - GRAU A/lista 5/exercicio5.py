# 5. Utilizando o template de menus mostrado em aula, faça um programa que simule uma calculadora simples, mostrando ao usuário as opções somar, subtrair, multiplicar e dividir dois números reais. Cada 
# uma das operações deve ser executada em funções que recebam como parâmetro os dois números, lidos do usuário. As funções devem retornar o resultado para o programa principal, que o exibirá na tela. 
# OBS.: Apenas chame a função de dividir se o divisor for diferente de zero (divisão por zero não existe!).

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Erro: Divisão por zero!"

def main():
    print("Calculadora Simples")
    print("Escolha a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    escolha = input("Digite o número da operação desejada: ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado da soma:", somar(num1, num2))
    elif escolha == '2':
        print("Resultado da subtração:", subtrair(num1, num2))
    elif escolha == '3':
        print("Resultado da multiplicação:", multiplicar(num1, num2))
    elif escolha == '4':
        print("Resultado da divisão:", dividir(num1, num2))
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()