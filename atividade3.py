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
    print("3. Sair")
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
