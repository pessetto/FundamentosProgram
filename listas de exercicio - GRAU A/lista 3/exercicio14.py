# 14) Criar um programa para identificar o valor a ser pago por um plano de saúde dada a idade do conveniado considerando que todos pagam R$ 300 e mais um adicional (se tiver dependentes) conforme a seguinte tabela:
# a) crianças com menos de 10 anos pagam R$100;
# b) dependentes com idade entre 10 e 30 anos pagam R$220;
# c) dependentes com idade entre 31 e 60 anos pagam R$ 395; 
# d) dependentes com mais de 60 anos pagam R$ 480
        
precoProduto = float(input("insira o preco do produto: "))

print("Formas de pagamento:")
print("1 - à vista em dinheiro")
print("2 - à vista no cartão de crédito")
print("3 - em duas vezes")
print("4 - em três vezes")

pagamento = int(input("escolha uma opcao: "))

if pagamento == 1:
    valorFinal = precoProduto * 0.85  
    
elif pagamento == 2:
    valorFinal = precoProduto * 0.90  
    
elif pagamento == 3:
    valorFinal = precoProduto  
    
elif pagamento == 4:
    valorFinal = precoProduto * 1.10  
    
else:
    valorFinal = "erro"

print(f"O valor a ser pago pelo produto é: R${valorFinal:.2f}")