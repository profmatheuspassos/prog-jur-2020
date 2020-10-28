while True:
    linha = input("Digite qualquer coisa, digite \"fim\" para terminar ou digite \"novo\" para digitar nova palavra: ")
    if linha == "novo":
        continue
    if linha == "fim":
        break
    print(linha)
print("Fim!")
