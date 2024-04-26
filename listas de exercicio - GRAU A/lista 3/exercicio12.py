# 12) A confederação brasileira de natação irá promover eliminatórias para o próximo mundial. Fazer um algoritmo que receba a idade de um nadador e imprima a sua categoria segundo a tabela a seguir:
# Categoria Idade
# Infantil A 5-7 anos
# Infantil B 8-10 anos
# Juvenil A 11-13 anos
# Juvenil B 14-17 anos
# Sênior Maiores de 18 anos
        
grauA = float(input("insira a nota do grau A: "))
grauB = float(input("insira a nota do grau B: "))
mediaFinal = ((grauA + grauB*2)/3)

print(f"a média final será: {format(mediaFinal, '.2f')}")

if mediaFinal >= 6:
    print("o aluno passou por media")
else:
    print("o aluno ficou em recuperacao")
    grauC = float(input("insira a nota do grau C: "))
    substituir = input("substituir a nota do grau A (A) ou do grau B (B)? ").upper()
    
    if substituir == "A":
        mediaFinal = ((grauC + grauB*2)/3)
    elif substituir == "B":
        mediaFinal = ((grauA + grauC*2)/3)
    else: 
        print("erro")
        
    if mediaFinal >= 6:
        print("media o aluno foi aprovado com média", format(mediaFinal, '.2f'))
    else:
        print("o aluno foi reprovado com média", format(mediaFinal, '.2f'))
