soma = 0
while True: # com o True o código executa “eternamente”
    num = int(input("Digite um número a somar ou 0 para sair: "))
    if num == 0:
        break
    soma = soma + num
print("O somatório de todos os números inseridos equivale a %d." %soma)
