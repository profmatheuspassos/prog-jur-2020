salario = float(input("Digite seu salário: "))
pc_aumento = 0.15
if salario > 1500:
    pc_aumento = 0.1
# aumento = salario * pc_aumento
# print("Seu aumento será de € %.2f." %aumento)
print("Seu aumento será de € %.2f." %(salario * pc_aumento))
