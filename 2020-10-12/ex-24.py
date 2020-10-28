x = input("Digite um número: ")
try:
    x = int(x)
    if x > 0:
        print("X é um número positivo.")
except:
    print("Você não digitou um número.")
