frase = input("Digite uma frase qualquer: ")
numero = float(input("Digite um número qualquer: "))
analise_frase = type(frase) == str
analise_numero = type(numero) == float
analise_final = type(frase) == type(numero)
print("\n")
print("A frase é do tipo str? " + str(analise_frase))
print("O número é do tipo float? " + str(analise_numero))
print("A frase é igual ao número? " + str(analise_final))
print("\n")
print("A frase é do tipo str? %s." %analise_frase)
print("O número é do tipo float? %s." %analise_numero)
print("A frase é igual ao número? %s." %analise_final)
"""
frase = input("Digite uma frase qualquer: ")
numero = float(input("Digite um número qualquer: "))
print("A frase é do tipo str? " + str(type(frase) == str))
print("O número é do tipo float? " + str(type(numero) == float))
print("A frase é igual ao número? " + str(type(frase) == type(numero)))
"""
