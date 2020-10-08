valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário mensal: "))
anos = int(input("Quantos anos para pagar: "))
meses = anos * 12
prestacao = valor / meses
if prestacao > salario * 0.3:
    print("Valor da prestação: € %.2f." %prestacao)
    print("Infelizmente você não pode obter o empréstimo. Trabalhe mais para aumentar seu salário.")
else:
    print("Empréstimo autorizado. Valor da prestação: € %.2f." %prestacao)
