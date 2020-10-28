print("Calculadora completa")
num1 = input("Digite o primeiro número: ")
operador = input("Digite um operador matemático (+, -, *, /): ")
num2 = input("Digite o segundo número: ")
msg_op = False
try:
    num1 = float(num1)
    num2 = float(num2)
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        resultado = num1 / num2
    else:
        msg_op = True
    print("Resultado: " + str(resultado))
    if resultado == int(resultado):
        print("O resultado é um número inteiro.")
    else:
        print("O resultado é um número decimal.")
except:
    if msg_op:
        print("O operador matemático digitado é inválido.")
    else:
        print("Digite apenas números, por favor.")
