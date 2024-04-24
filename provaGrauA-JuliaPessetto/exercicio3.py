# 3. (5 pts) Você foi contratado para desenvolver um programa que auxilie um velho alquimista a controlar o estoque dos seus ingredientes para preparar suas poções. O programa oferece um menu com 3 opções: preparar poção, consultar os ingredientes disponíveis e sair. Se o usuário optar por consultar os ingredientes, deve ser listado o nome de cada ingrediente e a quantidade atual de cada um. Tabela 1 mostra os ingredientes e suas quantidades iniciais que você deve assumir no programa. Se o usuário optar por preparar poção, você:

# a) Deve pedir para ele o número da poção a ser preparada. Tabela 2 mostra as poções e a quantidade de ingredientes que cada uma leva;
# b) Verificar se existe a quantidade de ingredientes suficientes para preparar a poção escolhida. Se não houver, você deverá imprimir uma mensagem dizendo qual (ou quais) os ingredientes estão faltando. Se tiver todos os ingredientes, você deve descontar essas quantidades dos ingredientes, e imprimir a mensagem: poção criada com sucesso! 

# Tabela 1. Lista de Ingredientes com sua quantidade inicial
# Ingrediente Quantidade inicial
# Pó de Fênix - 100 g
# Essência Celestial - 50 ml
# Raiz de Dragão - 45g
# Orvalho Lunar - 30 ml
# Flores secas - 200 g
# Elixir amargo - 20 ml
# Lágrimas de unicórnio - 15 ml

# Tabela 2. Poções e seus ingredientes de preparo
# # Poção Ingredientes
# 1 Poção de Cura -  Pó de Fênix (30g), Essência Celestial (20 ml), Flores secas
# (20g), Lágrimas de unicórnio (10 ml)
# 2 Poção Força da Floresta -  Orvalho Lunar (20 ml), Raiz de Dragão (30g), Flores secas (30g)
# 3  Poção Sabedoria da Riqueza -  Essência Celestial (30 ml), Pó de Fênix (50g)
# 4 Poção Sorte no Amor -  Orvalho Lunar (10 ml), Flores secas (50g), Lágrimas de
# unicórnio (5 ml)
# 5 Poção Malvada -  Elixir amargo (10 ml), Raiz de Dragão (15g)    
#--------------------------------------------------------------------------------------------------------------
#RESPOSTA:

# Dicionário contendo os ingredientes e suas quantidades iniciais
ingredientes = {
    "Pó de Fênix": 100,
    "Essência Celestial": 50,
    "Raiz de Dragão": 45,
    "Orvalho Lunar": 30,
    "Flores secas": 200,
    "Elixir amargo": 20,
    "Lágrimas de unicórnio": 15
}

# Dicionário contendo as poções e seus ingredientes
poções = {
    1: {"nome": "Poção de Cura", "ingredientes": {"Pó de Fênix": 30, "Essência Celestial": 20, "Flores secas": 20, "Lágrimas de unicórnio": 10}},
    2: {"nome": "Poção Força da Floresta", "ingredientes": {"Orvalho Lunar": 20, "Raiz de Dragão": 30, "Flores secas": 30}},
    3: {"nome": "Poção Sabedoria da Riqueza", "ingredientes": {"Essência Celestial": 30, "Pó de Fênix": 50}},
    4: {"nome": "Poção Sorte no Amor", "ingredientes": {"Orvalho Lunar": 10, "Flores secas": 50, "Lágrimas de unicórnio": 5}},
    5: {"nome": "Poção Malvada", "ingredientes": {"Elixir amargo": 10, "Raiz de Dragão": 15}}
}

# Função para consultar os ingredientes disponíveis
def consultarIngredientes():
    print("Ingredientes disponíveis:")
    for ingrediente, quantidade in ingredientes.items():
        print(f"{ingrediente}: {quantidade}")

# Função para preparar poção
def prepararPoção():
    numero_poção = int(input("Digite o número da poção que deseja preparar: "))
    poção = poções.get(numero_poção)
    
    if poção:
        ingredientes_necessarios = poção["ingredientes"]
        ingredientes_suficientes = True
        
        for ingrediente, quantidade_necessaria in ingredientes_necessarios.items():
            if ingrediente not in ingredientes or ingredientes[ingrediente] < quantidade_necessaria:
                print(f"Falta de {ingrediente} para preparar a poção.")
                ingredientes_suficientes = False
        
        if ingredientes_suficientes:
            for ingrediente, quantidade_necessaria in ingredientes_necessarios.items():
                ingredientes[ingrediente] -= quantidade_necessaria
            print("Poção criada com sucesso!")
    else:
        print("Número de poção inválido.")

# Menu principal
while True:
    print("\nMenu:")
    print("1. Preparar poção")
    print("2. Consultar ingredientes disponíveis")
    print("3. Sair \n")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        prepararPoção()
    elif opcao == 2:
        consultarIngredientes()
    elif opcao == 3:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")