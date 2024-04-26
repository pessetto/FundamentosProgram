# 5. Para x alunos da Unisinos, ler as notas do grau A e grau B e calcular a média considerando o sistema de notas da Unisinos. Se o aluno estiver aprovado escrever “APROVADO”. Caso contrário, ler o grau C
# e pedir qual o grau que deve ser substituído (A ou B, maiúsculo ou minúsculo), recalcular a média. Se estiver aprovado, escrever “APROVADO”, caso contrário escrever “REPROVADO”. No final escrever a média geral dos alunos.

def calcular_media(nota_a, nota_b):
    return (nota_a + 2*nota_b) / 3

def verificar_aprovacao(media):
    if media >= 6.0:
        return "APROVADO"
    else:
        return "REPROVADO"

def substituir_nota(nota_a, nota_b, nova_nota, substituir):
    if substituir.upper() == 'A':
        nota_a = nova_nota
    elif substituir.upper() == 'B':
        nota_b = nova_nota
    return nota_a, nota_b

def main():
    num_alunos = int(input("Digite o número de alunos: "))
    soma_notas_geral = 0

    for aluno in range(1, num_alunos + 1):
        print(f"Aluno {aluno}:")
        nota_a = float(input("Digite a nota do grau A: "))
        nota_b = float(input("Digite a nota do grau B: "))

        media = calcular_media(nota_a, nota_b)
        aprovacao = verificar_aprovacao(media)
        print(f"Situação: {aprovacao}")

        if aprovacao == "REPROVADO":
            nova_nota = float(input("Digite a nota do grau C: "))
            substituir = input("Qual nota (A ou B) deve ser substituída? ").strip()
            nota_a, nota_b = substituir_nota(nota_a, nota_b, nova_nota, substituir)
            media = calcular_media(nota_a, nota_b)
            aprovacao = verificar_aprovacao(media)
            print(f"Situação após substituição: {aprovacao}")

        soma_notas_geral += media

    media_geral = soma_notas_geral / num_alunos
    print(f"Média geral dos alunos: {media_geral:.2f}")

if __name__ == "__main__":
    main()