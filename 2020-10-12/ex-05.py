while True:
    ultimo = int(input("Digite o último número a ser mostrado: "))
    x = 1
    if ultimo < x:
        print("Por favor, digite apenas números positivos.")
    elif ultimo == x:
        print(x)
    else:
        while x <= ultimo:
            print(x)
            x = x + 1
