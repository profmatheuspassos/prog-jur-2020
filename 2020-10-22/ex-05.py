import math
def elevado_ao_cubo(n):
    print(str(n) + " elevado ao cubo é igual a " + str(n**3) + ".")
    print("%s elevado ao cubo é igual a " %n + str(n**3) + ".")
num = int(input("Digite um número para elevá-lo ao cubo: "))
elevado_ao_cubo(num)
