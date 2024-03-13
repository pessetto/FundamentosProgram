# Lista de Exercícios 1 – Fundamentos de Programação
# Comandos de Entrada/Saída e Variáveis
# 1. Utilizando o OnlineGDB, pesquise e implemente um programa que escreva na tela “Olá Mundo!” em 3 linguagens de programação diferentes. Qual é o comando de saída de dados nestas 3 linguagens?

JAVA:
public class Main
{
	public static void main(String[] args) {
		System.out.println("Hello World");
	}
}

C#:
using System;
class HelloWorld {
  static void Main() {
    Console.WriteLine("Hello World");
  }
}

RUBY:
puts "Hello World"


# 2. Escreva um programa em linguagem Python que solicite o nome do usuário e, em seguida, imprima uma mensagem de boas-vindas na tela, utilizando o nome fornecido.

nome = input("insira seu nome: ")
print ('Boas vindas,', nome)


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



# 4. Como poderíamos tornar o programa acima mais genérico, de maneira que pudéssemos registrar qualquer questão objetiva com 5 alternativas?

pergunta = "Qual é o verdadeiro nome do super-herói Batman?"

A = "A) Bruce Wayne"
B = "B) Clark Kent"
C = "C) Peter Parker"
D = "D) Tony Stark"
E = "E) Steve Rogers"

alternativas = [A, B, C, D, E]

print(pergunta)

for i in (alternativas):
    print(i)

gabarito = alternativas[0]

resposta_usuario = input("Digite sua resposta: ").upper()

print("Você respondeu alternativa", resposta_usuario, ". A responta correta era a alternativa", gabarito)
