salario = float(input("Digite o salário atual: "))
p_aumento = float(input("Digite a porcentagem de aumento: "))
aumento = salario * p_aumento / 100
novo_salario = salario + aumento
print("Um aumento de %.2f%% em um salário de %.2f euros" %(p_aumento, salario))
print("é igual a um aumento de %.2f euros," %aumento)
print("resultando em um novo salário de %.2f euros." %novo_salario)
