horas_semana = float(input("Digite o número de horas por semana: "))
valor_por_hora = float(input("Digite o valor pago por hora: "))
print("Salário bruto por mês: " + str(int((horas_semana * valor_por_hora) * 4)) + " euros.")
