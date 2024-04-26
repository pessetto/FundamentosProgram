# 3. Escreva um programa em Python que realize o seguinte procedimento:
#   a. Imprima na tela a seguinte questão: Qual é o verdadeiro nome do super-herói Batman?
#   b. Apresente cinco alternativas para o usuário, cada uma em uma linha: a) Bruce Wayne b) Clark Kent c) Peter Parker d) Tony Stark e) Steve Rogers
#   c. Armazene a letra correspondente à resposta correta (‘a’) em uma variável.
#   d. Solicite ao usuário que digite sua resposta, e a armazene em uma variável.
#   e. Ao final, o programa deve exibir na tela a resposta do usuário e a resposta correta. Por exemplo, se o usuário digitou como resposta a alternativa ‘d’, a mensagem seria esta: Você respondeu alternativa d. A resposta correta é a alternativa a.

print("Qual é o verdadeiro nome do super-herói Batman?")

print("alternativas:")
print("A) Bruce Wayne")
print("B) Clark Kent")
print("C) Peter Parker")
print("D) Tony Stark")
print("E) Steve Rogers")

resposta = 'A'

respostaUsuario = input("Digite sua resposta: ")

if (resposta == respostaUsuario.upper()):
    print("Você acertou!!!")
else:
    print("Você respondeu alternativa", respostaUsuario, ". A responta correta era a alternativa 'A'.")
