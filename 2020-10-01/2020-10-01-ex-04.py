preco = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))
valor_do_desconto = preco * desconto / 100
a_pagar = preco - valor_do_desconto
print("Um desconto de %.2f%% em uma mercadoria de %.2f euros" %(desconto, preco))
print("equivale a %.2f euros." %valor_do_desconto)
print("O valor a pagar é de %.2f euros." %a_pagar)
