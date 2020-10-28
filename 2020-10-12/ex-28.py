print("Calculadora 1.0\n")
print("Siga as instruções ou digite \"sair\" para terminar o programa.\n")
while True:
    num1 = input("Digite o primeiro número: ")
    if num1 == "sair":
        break
    try:
        num1 = float(num1)
    except:
        print("\nPor favor, digite apenas números ou \"sair\" para terminar o programa.\n")
        continue
    num2 = input("Digite o segundo número: ")
    if num2 == "sair":
        break
    try:
        num2 = float(num2)
    except:
        print("\nPor favor, digite apenas números ou \"sair\" para terminar o programa.\n")
        continue
    operador = input("Digite o operador matemático (+, -, *, /): ")
    if operador == "sair":
        break
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        resultado = num1 / num2
    else:
        print("\nPor favor, digite um operador matemático válido ou \"sair\" para terminar o programa.\n")
        continue
    print("Resultado da operação: %.2f.\n" %resultado)
print("\nObrigado por utilizar a Calculadora 1.0.\n")
