def calculaSalario(a, b):
    return int(a * b * 4)

while True:
    while True:
        valorPorHora = input("Digite o valor pago por hora: ")
        try:
            valorPorHora = int(valorPorHora)
            break
        except:
            print("Por favor, insira apenas números.")
            continue
    while True:
        quantidadeHoras = input("Digite o número de horas trabalhadas por semana ou \"-1\" para encerrar: ")
        try:
            quantidadeHoras = int(quantidadeHoras)
            break
        except:
            print("Por favor, insira apenas números.")
            continue
    if quantidadeHoras == -1:
        print("Obrigado por utilizar nosso programa.\n")
#    break
        break
    salarioBruto = calculaSalario(valorPorHora, quantidadeHoras)
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
    print("Salário líquido: " + str(salarioLiquido) + "€/mês.\n")
