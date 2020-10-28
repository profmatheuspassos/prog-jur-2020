soma = 0
quantidade = 0
while True:
    num = int(input("Digite um número inteiro: "))
    if num == 0:
        break;
    soma = soma + num
    quantidade = quantidade + 1
print("Quantidade de números digitados: %d." %quantidade)
print("Soma: %d." %soma)
print("Média: %.2f." %(soma/quantidade))
