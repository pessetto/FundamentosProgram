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

import random

# Inventário inicial do jogador
inventario = {
    "comum": 0,
    "raro": 0,
    "lendario": 0
}

def abrir_caixa():
    # Probabilidade de obtenção de cada tipo de item
    tipos_de_item = ['comum'] * 80 + ['raro'] * 19 + ['lendario'] * 1

    # Escolha aleatória do tipo de item
    tipo_obtido = random.choice(tipos_de_item)

    # Atualiza o inventário do jogador
    inventario[tipo_obtido] += 1

    print(f"Você coletou 1 item {tipo_obtido}!")

def consultar_itens():
    print("Itens coletados:")
    for tipo, quantidade in inventario.items():
        print(f"Itens {tipo}: {quantidade}")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Abrir uma caixa")
        print("2 - Consultar itens")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            abrir_caixa()
        elif opcao == "2":
            consultar_itens()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    menu()