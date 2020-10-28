x = input("Digite um número: ")
try:
    x = int(x)
    if x > 0:
        print("X é um número positivo.")
    elif x == 0:
        print("X é igual a zero.")
    else:
        print("X é um número negativo.")
except:
    print("Você não digitou um número.")
