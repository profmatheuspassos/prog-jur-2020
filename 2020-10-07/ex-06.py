distancia = float(input("Digite a distância a percorrer: "))
if distancia <= 200:
    passagem = 0.5 * distancia
else:
    passagem = 0.45 * distancia
print("Preço da passagem: € %.2f." %passagem)
