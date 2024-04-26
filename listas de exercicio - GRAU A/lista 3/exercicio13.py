# 13) Faça um programa que leia a nota do Grau A e do Grau B do aluno e calcule a média final conforme as regras da Unisinos. Imprima a média final na tela e diga se o aluno passou por média ou se ficou em recuperação (grau C). Se o aluno ficou em recuperação, pergunte se ele quer substituir o Grau A ou o Grau B (ele deve digitar ‘a’ ou ‘b’). Leia a nota do Grau C, recalcule a média de acordo com o grau substituído e imprima na tela o resultado, informando se ele foi aprovado ou reprovado.
        
valorAdicional = 0

idadeConveniado = int(input("insira a idade do conveniado: "))
qtdDependentes = int(input("insira a quantidade de dependentes: "))

if idadeConveniado < 10:
    valorAdicional += 100
    
elif 10 <= idadeConveniado <= 30:
    valorAdicional += 220
    
elif 31 <= idadeConveniado <= 60:
    valorAdicional += 395
    
else:
    valorAdicional += 480

for i in range(qtdDependentes):
    idadeDependente = int(input(f"insira a idade do dependente {i + 1}: "))
    
    if idadeDependente < 10:
        valorAdicional += 100
        
    elif 10 <= idadeDependente <= 30:
        valorAdicional += 220
        
    elif 31 <= idadeDependente <= 60:
        valorAdicional += 395
        
    else:
        valorAdicional += 480

valorTotal = 300 + (valorAdicional * qtdDependentes)

print(f"o valor do plano de saúde sera: R${valorTotal:.2f}")