# 3. Implemente uma função mediaUnisinos que receba como parâmetro as notas do Grau A e do Grau B e retorne o resultado do grau final.

def mediaUnisinos(nota_grau_a, nota_grau_b):
    # Calcula a média ponderada das notas, considerando o sistema de pesos da Unisinos
    # O Grau A tem peso 4 e o Grau B tem peso 6
    media_final = (nota_grau_a + nota_grau_b * 2) / 3
    return media_final

# Exemplo de uso da função mediaUnisinos
nota_a = float(input("Digite a nota do Grau A: "))
nota_b = float(input("Digite a nota do Grau B: "))
resultado_final = mediaUnisinos(nota_a, nota_b)
print("O resultado do Grau Final é:", resultado_final)
