consumo = int(input("Consumo em kWh: "))
tipo = input("Tipo da instalação (R, C ou I): ")
if tipo == "R":
    if consumo <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif tipo == "C":
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.6
elif tipo == "I":
    if consumo <= 5000:
        preco = 0.5
    else:
        preco = 0.65
else:
    preco = 0
    print("Erro! Tipo de instalação desconhecido!")
custo = consumo * preco
print("Valor a pagar: € %.2f." %custo)
