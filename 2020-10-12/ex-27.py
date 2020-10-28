score = float(input("Digite a sua nota com valores entre 0.0 e 1,0: "))
if score > 1:
    print("O número deve ser entre 0.0 e 1.0!")
elif score < 0:
    print("O número deve ser entre 0.0 e 1.0!")
elif score >= 0.9:
    print("Superior")
elif score >= 0.8:
    print("Médio superior")
elif score >= 0.7:
    print("Médio")
elif score >= 0.6:
    print("Médio inferior")
else:
    print("Insuficiente")
