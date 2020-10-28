temp_usuario = input("Insira a temperatura em Fahrenheit: ")
try:
    temp_fahr = float(temp_usuario)
    print("A temperatura em Celsius é igual a %.2f graus." %((temp_fahr - 32.0) * 5.0 / 9.0))
except:
    print("Por favor, digite apenas números.")
