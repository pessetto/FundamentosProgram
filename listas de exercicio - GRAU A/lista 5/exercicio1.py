# 1. Implemente uma função cumprimentar que receba como parâmetro o nome de uma pessoa e escreva a mensagem “Olá, <nome_da_pessoa>!”

def cumprimentar(nome_da_pessoa):
    print(f"Olá, {nome_da_pessoa}!")

# Exemplo de uso da função cumprimentar
nome = input("Digite o nome da pessoa: ")
cumprimentar(nome)