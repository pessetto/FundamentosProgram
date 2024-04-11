# # Definir funções

# def minhaFuncao():
#     print("Olá Funções")

# # Código principal

# print("olá!")

# minhaFuncao()




# ___________________________EXERCICIO 1__________________________________
# Funções________________________________________________________________
# def cumprimentar(nome):
#     print("Olá,", nome, "!")

# # Código principal_______________________________________________________

# # nome1 = input("Digite o nome do primeiro usuario: ")
# # cumprimentar(nome1)

# # nome2 = input("Digite o nome do segundo usuario: ")
# # cumprimentar(nome2)

# for i in range(5):
#     print("Usuario", i+1, end = "")
#     nome = input(", digite seu nome: ")
#     cumprimentar(nome)




# ___________________________EXERCICIO 2__________________________________
# Funções________________________________________________________________
# def tabuada(n):
#     for i in range(1,11):
#         print(n, "X", i, "=", n * i)

# # Código principal_______________________________________________________
# n = int(input("Digite o numero para ver sua tabuada: "))
# tabuada(n)



# ___________________________EXERCICIO 3 ELEFANTES_______________________
# Funções________________________________________________________________
# def musicaElefante(n):
#     for i in range(1,n):
#         print(i, " elefantes incomodam muito a gente")
#         print(i+1 , " elefantes ", end ="")
#         for j in range(0, i+1):
#             print("incomodam, ", end ="")
#         print("muito mais!")


# # Código principal_______________________________________________________

# musicaElefante(2)



# ___________________________EXERCICIO 4_________________________________
# Funções________________________________________________________________
def mediaUnisinos(grauA, grauB):
    media = (grauA + 2* grauB) / 3.0
    return media

# Código principal_______________________________________________________

grauA = float(input("Digite sua média do grau A: "))
grauB = float(input("Digite sua média do grau B: "))

grauFinal = mediaUnisinos(grauA, grauB)
print("Grau final é: ", grauFinal)
