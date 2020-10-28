valorPorHora = input("Digite o valor pago por hora: ")
quantidadeHoras = input("Digite o número de horas trabalhadas por semana: ")
try:
    salarioBruto = (int(valorPorHora) * int(quantidadeHoras)) * 4
    if salarioBruto > 2401:
        irs = 32
    elif salarioBruto > 1801:
        irs = 24
    elif salarioBruto > 1201:
        irs = 16
    elif salarioBruto > 601:
        irs = 8
    else:
        irs = 0
    valorIRS = int(salarioBruto * (irs / 100))
    valorSS = int(salarioBruto * (11 / 100))
    salarioLiquido = int(salarioBruto - valorIRS - valorSS)
    print("Salário bruto: " + str(salarioBruto) + "€/mês.")
    print("Desconto do IRS (" + str(irs) + "% do salário bruto): " + str(valorIRS) + "€.")
    print("Desconto da Segurança Social (11% do salário bruto): " + str(valorSS) + "€.")
    print("Valor total dos descontos: " + str(valorSS + valorIRS) + "€.")
    print("Salário líquido: " + str(salarioLiquido) + "€/mês.")
except:
    print("Por favor, insira apenas números.")
