x = 1
soma = 0
while x <= 5:
     n = int(input("Digite o %dº número: " %x))
     soma = soma + n
     x = x + 1
print("Média: %.2f." %(soma/5))
