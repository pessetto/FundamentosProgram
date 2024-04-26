# 1. Implemente uma função cumprimentar que receba como parâmetro o nome de uma pessoa e escreva a mensagem “Olá, <nome_da_pessoa>!”

# def cumprimentar(nome_da_pessoa):
#     print(f"Olá, {nome_da_pessoa}!")

# # Exemplo de uso da função cumprimentar
# nome = input("Digite o nome da pessoa: ")
# cumprimentar(nome)

#-------------------------------------------------------------------------------------------------------------------#
# 2. Implemente uma função tabuada que receba como parâmetro um número inteiro e escreva a tabuada desse número.

# def tabuada(numero):
#     print(f"Tabuada do {numero}:")
#     for i in range(1, 11):
#         resultado = numero * i
#         print(f"{numero} x {i} = {resultado}")

# # Exemplo de uso da função tabuada
# num = int(input("Digite um número inteiro: "))
# tabuada(num)


#-------------------------------------------------------------------------------------------------------------------#
# 3. Implemente uma função mediaUnisinos que receba como parâmetro as notas do Grau A e do Grau B e retorne o resultado do grau final.
# def mediaUnisinos(nota_grau_a, nota_grau_b):
#     # Calcula a média ponderada das notas, considerando o sistema de pesos da Unisinos
#     # O Grau A tem peso 4 e o Grau B tem peso 6
#     media_final = (nota_grau_a + nota_grau_b * 2) / 3
#     return media_final

# # Exemplo de uso da função mediaUnisinos
# nota_a = float(input("Digite a nota do Grau A: "))
# nota_b = float(input("Digite a nota do Grau B: "))
# resultado_final = mediaUnisinos(nota_a, nota_b)
# print("O resultado do Grau Final é:", resultado_final)

#-------------------------------------------------------------------------------------------------------------------#
# 4. Implemente uma função sorteio que receba o intervalo de valores inteiros início e fim como parâmetro e sorteie um número dentro do intervalo (considerando intervalo fechado [início, fim])

# import random

# def sorteio(inicio, fim):
#     # Sorteia um número inteiro dentro do intervalo [inicio, fim]
#     numero_sorteado = random.randint(inicio, fim)
#     return numero_sorteado

# # Exemplo de uso da função sorteio
# inicio_intervalo = int(input("Digite o início do intervalo: "))
# fim_intervalo = int(input("Digite o fim do intervalo: "))
# numero_sorteado = sorteio(inicio_intervalo, fim_intervalo)
# print("Número sorteado:", numero_sorteado)


#-------------------------------------------------------------------------------------------------------------------#
# 5. Utilizando o template de menus mostrado em aula, faça um programa que simule uma calculadora simples, mostrando ao usuário as opções somar, subtrair, multiplicar e dividir dois números reais. Cada 
# uma das operações deve ser executada em funções que recebam como parâmetro os dois números, lidos do usuário. As funções devem retornar o resultado para o programa principal, que o exibirá na tela. 
# OBS.: Apenas chame a função de dividir se o divisor for diferente de zero (divisão por zero não existe!).

# def somar(num1, num2):
#     return num1 + num2

# def subtrair(num1, num2):
#     return num1 - num2

# def multiplicar(num1, num2):
#     return num1 * num2

# def dividir(num1, num2):
#     if num2 != 0:
#         return num1 / num2
#     else:
#         return "Erro: Divisão por zero!"

# def main():
#     print("Calculadora Simples")
#     print("Escolha a operação:")
#     print("1. Somar")
#     print("2. Subtrair")
#     print("3. Multiplicar")
#     print("4. Dividir")

#     escolha = input("Digite o número da operação desejada: ")

#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))

#     if escolha == '1':
#         print("Resultado da soma:", somar(num1, num2))
#     elif escolha == '2':
#         print("Resultado da subtração:", subtrair(num1, num2))
#     elif escolha == '3':
#         print("Resultado da multiplicação:", multiplicar(num1, num2))
#     elif escolha == '4':
#         print("Resultado da divisão:", dividir(num1, num2))
#     else:
#         print("Opção inválida!")

# if __name__ == "__main__":
#     main()


#-------------------------------------------------------------------------------------------------------------------#
# 6. Utilizando o template de menus mostrado em aula, faça um programa que simule um sistema de lootbox simples. As opções para o usuário são abrir uma caixa e consultar itens coletados. Ao abrir uma caixa, o
# usuário irá receber 1 item comum, raro ou lendário, conforme a probabilidade da tabela abaixo:
# Tipo de item Probabilidade de obtenção
# Comum 80 %
# Raro 19%
# Lendário 1%

# Ao obter o item, deverá se atualizar o inventário do jogador contabilizando o número de itens comuns,
# raros e lendários que ele possui. Ao consultar os itens coletados, deverá ser mostrado ao usuário a
# quantidade de itens de cada tipo que ele possui.
# Exemplos de tela:
# 1 – Abrir uma caixa
# 2 – Consultar itens
# 0 - Sair

# Escolha uma opção: 1
# Você coletou 1 item comum!
# 1 – Abrir uma caixa
# 2 – Consultar itens
# 0 - Sair
# -----
# Escolha uma opção: 2
# Itens comuns: 9
# Itens raros: 2
# Itens lendários: 0

# import random

# # Inventário inicial do jogador
# inventario = {
#     "comum": 0,
#     "raro": 0,
#     "lendario": 0
# }

# def abrir_caixa():
#     # Probabilidade de obtenção de cada tipo de item
#     tipos_de_item = ['comum'] * 80 + ['raro'] * 19 + ['lendario'] * 1

#     # Escolha aleatória do tipo de item
#     tipo_obtido = random.choice(tipos_de_item)

#     # Atualiza o inventário do jogador
#     inventario[tipo_obtido] += 1

#     print(f"Você coletou 1 item {tipo_obtido}!")

# def consultar_itens():
#     print("Itens coletados:")
#     for tipo, quantidade in inventario.items():
#         print(f"Itens {tipo}: {quantidade}")

# def menu():
#     while True:
#         print("\nMenu:")
#         print("1 - Abrir uma caixa")
#         print("2 - Consultar itens")
#         print("0 - Sair")

#         opcao = input("Escolha uma opção: ")

#         if opcao == "1":
#             abrir_caixa()
#         elif opcao == "2":
#             consultar_itens()
#         elif opcao == "0":
#             print("Saindo do programa...")
#             break
#         else:
#             print("Opção inválida. Por favor, escolha novamente.")

# if __name__ == "__main__":
#     menu()
