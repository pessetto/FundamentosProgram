# 7) Implementar um programa que calcula o desconto previdenciário de um funcionário. O programa deve, dado um salário retornar o valor do desconto proporcional ao mesmo. O cálculo de desconto segue a regra: o desconto deve 11% do valor do salário. Entretanto, o valor máximo de desconto é 318,20. Sendo assim, ou o método retorna 11% sobre o salário ou 318,20.

salario = float(input('Digite o seu salário: '))

desconto = (salario * 0.11)
# salarioF = (salario * 0.89)

if desconto > 318.20:
    print('O desconto foi de R$318.20')

else:
    print('O desconto do seu salário foi de R$', desconto)