categoria = input("Digite a categoria do produto: ")
if categoria == "1":
    preco = 10
else:
    if categoria == "2":
       preco = 18
    else:
       if categoria == "3":
          preco = 23
       else:
          if categoria == "4":
             preco = 26
          else:
             if categoria == "5":
                preco = 31
             else:
                print("Categoria inválida, digite um valor entre 1 e 5!")
                preco = 0
print("O preço do produto é € %.2f." %preco)
print("A categoria inseria foi %s." %categoria)

"""
if categoria != "1" and categoria != "2" and categoria != "3" and categoria != "4" and categoria != "5":
    print("Categoria inválida, digite um valor entre 1 e 5!")
"""