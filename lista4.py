# # 1. Faça um algoritmo para:
# #   a. Gerar e escrever todos os números inteiros do intervalo [0,100].
# n = 0
# while n <= 100:
#       print(n)
#       n = n + 1

#-------------------------------------------------------------------------------------------------------------------#
#   # b. Gerar e escrever os números pares do intervalo [20,50].
# n = 20
# while n <= 50:
#       print(n)
#       n = n + 2

#-------------------------------------------------------------------------------------------------------------------#
#   # c. Gerar e escrever os números inteiros do intervalo [25,70] em ordem decrescente.
# n = 70
# while n >= 25:
#       print(n)
#       n = n - 1

#-------------------------------------------------------------------------------------------------------------------#
#   # d. Gerar e escrever os números ímpares do intervalo [25,95] em ordem decrescente.
#   n = 95
#   while n >= 25:
#       print(n)
#       n = n - 2

#-------------------------------------------------------------------------------------------------------------------# 
#   # e. Ler 15 números e escrever a soma e a média dos números lidos.
# def main():
#     # Inicializando variáveis para soma e contador
#     soma = 0
#     contador = 0

#     # Loop para ler os 15 números
#     for i in range(15):
#         # Solicitação de entrada do usuário e conversão para float
#         numero = float(input(f"Digite o {i+1}º número: "))
#         # Adiciona o número à soma
#         soma += numero
#         # Incrementa o contador
#         contador += 1

#     # Calcula a média
#     media = soma / contador

#     # Exibe a soma e a média
#     print(f"A soma dos números é: {soma}")
#     print(f"A média dos números é: {media}")

# # Chama a função principal
# if __name__ == "__main__":
#     main()

#-------------------------------------------------------------------------------------------------------------------#
#   # f. Ler 10 números inteiros e escrever a quantidade de números pares e a quantidade de números ímpares lidos.
# def main():
#     # Inicializando contadores para números pares e ímpares
#     pares = 0
#     impares = 0

#     # Loop para ler os 10 números
#     for i in range(10):
#         # Solicitação de entrada do usuário e conversão para int
#         numero = int(input(f"Digite o {i+1}º número: "))
#         # Verifica se o número é par ou ímpar e atualiza os contadores
#         if numero % 2 == 0:
#             pares += 1
#         else:
#             impares += 1

#     # Exibe a quantidade de números pares e ímpares
#     print(f"Quantidade de números pares: {pares}")
#     print(f"Quantidade de números ímpares: {impares}")

# # Chama a função principal
# if __name__ == "__main__":
#     main()

#-------------------------------------------------------------------------------------------------------------------#
#   # g. Sortear 20 números inteiros entre -10 e 10 e imprimi-los acompanhados da mensagem “POSITIVO”, “NEGATIVO”, ou “NULO”, conforme o caso. No final, imprimir a quantidade de números positivos e negativos lidos.

# import random

# def main():
#     # Inicializando contadores para números positivos e negativos
#     positivos = 0
#     negativos = 0

#     # Loop para sortear e imprimir os 20 números
#     for _ in range(20):
#         # Sorteia um número entre -10 e 10
#         numero = random.randint(-10, 10)
        
#         # Verifica se o número é positivo, negativo ou nulo e atualiza os contadores
#         if numero > 0:
#             print(f"{numero} - POSITIVO")
#             positivos += 1
#         elif numero < 0:
#             print(f"{numero} - NEGATIVO")
#             negativos += 1
#         else:
#             print(f"{numero} - NULO")

#     # Exibe a quantidade de números positivos e negativos
#     print(f"\nQuantidade de números positivos: {positivos}")
#     print(f"Quantidade de números negativos: {negativos}")

# # Chama a função principal
# if __name__ == "__main__":
#     main()

#-------------------------------------------------------------------------------------------------------------------#
#   # h. Ler n números e imprimir no final a soma dos números lidos (obs.: n é a quantidade de números que deverão ser lidos e também deve ser lido do teclado)

# def main():
#     # Solicitação da quantidade de números a serem lidos
#     n = int(input("Digite a quantidade de números a serem lidos: "))

#     # Inicializando variável para a soma
#     soma = 0

#     # Loop para ler os 'n' números
#     for i in range(n):
#         # Solicitação de entrada do usuário e conversão para int
#         numero = float(input(f"Digite o {i+1}º número: "))
#         # Adiciona o número à soma
#         soma += numero

#     # Exibe a soma dos números lidos
#     print(f"A soma dos números é: {soma}")

# # Chama a função principal
# if __name__ == "__main__":
#     main()



#-------------------------------------------------------------------------------------------------------------------#
# 2. Implemente um programa que sorteia um número de 1 a 10 e dá ao usuário 3 tentativas de acertá-lo. A cada tentativa errada, o programa informa se o número a adivinhar está abaixo ou acima.

# import random

# def main():
#     # Sorteia um número aleatório de 1 a 10
#     numero_secreto = random.randint(1, 10)
#     tentativas_restantes = 3

#     print("Bem-vindo ao jogo de adivinhação!")
#     print("Tente adivinhar um número de 1 a 10.")

#     while tentativas_restantes > 0:
#         try:
#             # Solicita ao usuário um palpite
#             palpite = int(input("Digite seu palpite: "))

#             # Verifica se o palpite está correto
#             if palpite == numero_secreto:
#                 print("Parabéns! Você acertou o número!")
#                 break
#             elif palpite < numero_secreto:
#                 print("O número a adivinhar está acima do seu palpite.")
#             else:
#                 print("O número a adivinhar está abaixo do seu palpite.")

#             tentativas_restantes -= 1
#             print(f"Tentativas restantes: {tentativas_restantes}")

#         except ValueError:
#             print("Por favor, digite um número válido.")

#     if tentativas_restantes == 0:
#         print(f"Suas tentativas acabaram. O número correto era {numero_secreto}.")

# if __name__ == "__main__":
#     main()


#-------------------------------------------------------------------------------------------------------------------#
# 3. Elabore um programa que lê um número de 1 a 9 e mostra a tabuada de multiplicação do número. Exemplo de tela de saída:
#   Entre com um número: 5
#   5 x 1 = 5
#   5 x 2 = 10
#   ...
#   5 x 10 = 50
#   Calcular outro número (s/n)? n

# def tabuada_multiplicacao():
#     while True:
#         try:
#             numero = int(input("Entre com um número de 1 a 9: "))
#             if 1 <= numero <= 9:
#                 for i in range(1, 11):
#                     resultado = numero * i
#                     print(f"{numero} x {i} = {resultado}")
#                 continuar = input("Calcular outro número (s/n)? ").strip().lower()
#                 if continuar != 's':
#                     break
#             else:
#                 print("Por favor, digite um número válido de 1 a 9.")
#         except ValueError:
#             print("Por favor, digite um número válido.")

# if __name__ == "__main__":
#     tabuada_multiplicacao()



#-------------------------------------------------------------------------------------------------------------------#
# 4. Escrever um programa que calcule todos os números divisíveis por certo valor indicado pelo usuário (o resto da divisão por este número deve ser igual a zero), compreendidos em um intervalo também
# especificado pelo usuário. O usuário deve entrar com um primeiro valor correspondente ao divisor e após ele vai fornecer o valor inicial do intervalo, seguido do valor final deste intervalo. Exemplo de tela de saída:
# Entre com o valor do divisor: 3 
# Início do intervalo: 17
# Final do intervalo: 29
# Números divisíveis por 3 no intervalo de 17 a 29:
# 18 21 24 27

# def numeros_divisiveis():
#     try:
#         divisor = int(input("Entre com o valor do divisor: "))
#         inicio_intervalo = int(input("Início do intervalo: "))
#         final_intervalo = int(input("Final do intervalo: "))

#         print(f"Números divisíveis por {divisor} no intervalo de {inicio_intervalo} a {final_intervalo}:")
#         for numero in range(inicio_intervalo, final_intervalo + 1):
#             if numero % divisor == 0:
#                 print(numero, end=" ")
#         print()  # Imprime uma linha em branco para melhor legibilidade

#     except ValueError:
#         print("Por favor, entre com valores inteiros válidos.")

# if __name__ == "__main__":
#     numeros_divisiveis()



#-------------------------------------------------------------------------------------------------------------------#
# 5. Para x alunos da Unisinos, ler as notas do grau A e grau B e calcular a média considerando o sistema de notas da Unisinos. Se o aluno estiver aprovado escrever “APROVADO”. Caso contrário, ler o grau C
# e pedir qual o grau que deve ser substituído (A ou B, maiúsculo ou minúsculo), recalcular a média. Se estiver aprovado, escrever “APROVADO”, caso contrário escrever “REPROVADO”. No final escrever a média geral dos alunos.

# def calcular_media(nota_a, nota_b):
#     return (nota_a + 2*nota_b) / 3

# def verificar_aprovacao(media):
#     if media >= 6.0:
#         return "APROVADO"
#     else:
#         return "REPROVADO"

# def substituir_nota(nota_a, nota_b, nova_nota, substituir):
#     if substituir.upper() == 'A':
#         nota_a = nova_nota
#     elif substituir.upper() == 'B':
#         nota_b = nova_nota
#     return nota_a, nota_b

# def main():
#     num_alunos = int(input("Digite o número de alunos: "))
#     soma_notas_geral = 0

#     for aluno in range(1, num_alunos + 1):
#         print(f"Aluno {aluno}:")
#         nota_a = float(input("Digite a nota do grau A: "))
#         nota_b = float(input("Digite a nota do grau B: "))

#         media = calcular_media(nota_a, nota_b)
#         aprovacao = verificar_aprovacao(media)
#         print(f"Situação: {aprovacao}")

#         if aprovacao == "REPROVADO":
#             nova_nota = float(input("Digite a nota do grau C: "))
#             substituir = input("Qual nota (A ou B) deve ser substituída? ").strip()
#             nota_a, nota_b = substituir_nota(nota_a, nota_b, nova_nota, substituir)
#             media = calcular_media(nota_a, nota_b)
#             aprovacao = verificar_aprovacao(media)
#             print(f"Situação após substituição: {aprovacao}")

#         soma_notas_geral += media

#     media_geral = soma_notas_geral / num_alunos
#     print(f"Média geral dos alunos: {media_geral:.2f}")

# if __name__ == "__main__":
#     main()


#-------------------------------------------------------------------------------------------------------------------#
# 6. Crie um algoritmo que sorteie 5 valores entre 0 e 100 e depois imprima o menor, o maior e a média dos valores sorteados.

# import random

# def main():
#     # Inicializa uma lista vazia para armazenar os valores sorteados
#     valores = []

#     # Sorteia 5 valores entre 0 e 100 e os adiciona à lista
#     for _ in range(5):
#         valores.append(random.randint(0, 100))

#     # Encontra o menor e o maior valor na lista
#     menor_valor = min(valores)
#     maior_valor = max(valores)

#     # Calcula a média dos valores
#     media_valores = sum(valores) / len(valores)

#     # Imprime os resultados
#     print("Valores sorteados:", valores)
#     print("Menor valor:", menor_valor)
#     print("Maior valor:", maior_valor)
#     print("Média dos valores:", media_valores)

# if __name__ == "__main__":
#     main()



#-------------------------------------------------------------------------------------------------------------------#
# 7. Descubra, dentre cinco nomes informados pelo usuário, qual o primeiro em ordem alfabética.

# def encontrar_primeiro_nome():
#     # Inicializa uma lista vazia para armazenar os nomes
#     nomes = []

#     # Solicita ao usuário que insira cinco nomes
#     for i in range(5):
#         nome = input(f"Digite o {i+1}º nome: ")
#         nomes.append(nome)

#     # Encontra o primeiro nome em ordem alfabética
#     primeiro_nome = min(nomes)

#     # Imprime o primeiro nome em ordem alfabética
#     print("O primeiro nome em ordem alfabética é:", primeiro_nome)

# if __name__ == "__main__":
#     encontrar_primeiro_nome()


#-------------------------------------------------------------------------------------------------------------------#
# 8. Fazer um programa que calcule e imprima o fatorial de um número fornecido pelo usuário. Repetir a execução do programa tantas até o usuário responder não. O fatorial de um número inteiro positivo é
# definido como o número multiplicado por ele menos 1, menos 2, etc até o valor 1. Por exemplo, o fatorial de 4 é 4x3x2x1=24. Exemplo de tela de saída:
# Entre com um número: 5
# O fatorial de 5 é 120
# Calcular outro número (s/n)? n

# def calcular_fatorial(numero):
#     # Caso especial: fatorial de 0 é 1
#     if numero == 0:
#         return 1
#     else:
#         # Inicializa o fatorial como 1
#         fatorial = 1
#         # Calcula o fatorial multiplicando o número por todos os inteiros de 1 até o número
#         for i in range(1, numero + 1):
#             fatorial *= i
#         return fatorial

# def main():
#     while True:
#         try:
#             numero = int(input("Entre com um número: "))
#             fatorial = calcular_fatorial(numero)
#             print(f"O fatorial de {numero} é {fatorial}")

#             calcular_outro = input("Calcular outro número (s/n)? ").strip().lower()
#             if calcular_outro != 's':
#                 break
#         except ValueError:
#             print("Por favor, digite um número inteiro válido.")

# if __name__ == "__main__":
#     main()


#-------------------------------------------------------------------------------------------------------------------#
# 9. Escrever um programa que produza a saída abaixo na tela, para n linhas e usando um caractere lido do teclado.
# Exemplo de tela de saída, para n = 5 e caracter = `*`:
# Entre com um número: 5
# Entre com um caracter: *
# *
# * *
# * * *
# * * * *
# * * * * *

# def imprimir_padrao(n, caractere):
#     for i in range(1, n + 1):
#         print(caractere * i)

# def main():
#     try:
#         n = int(input("Entre com um número: "))
#         caractere = input("Entre com um caractere: ")

#         imprimir_padrao(n, caractere)
#     except ValueError:
#         print("Por favor, digite um número inteiro válido.")

# if __name__ == "__main__":
#     main()
