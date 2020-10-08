a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
operacao = input("Digite a operação a realizar (+,-,* ou /): ")
if operacao == "+":
    resultado = a + b
elif operacao == "-":
    resultado = a - b
elif operacao == "*":
    resultado = a * b
elif operacao == "/":
    resultado = a / b
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado da operação: %.2f", %resultado)
