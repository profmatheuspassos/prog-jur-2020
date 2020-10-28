valor_a_pagar = 0
while True:
    codigo = int(input("Código da mercadoria (0 para sair): "))
    preco = 0
    if codigo == 0:
        break;
    elif codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif código == 9:
        codigo = 8.00
    else:
        print("Código inválido!")
    if codigo != 0:
        quantidade = int(input("Quantidade: "))
        valor_a_pagar = valor_a_pagar + (codigo * quantidade)
print("Total a pagar: € %.2f." %valor_a_pagar)
