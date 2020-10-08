print("Exercício 1")
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
print("A soma de %d mais %d é igual a %d." %(num1, num2, (num1 + num2)))
print("\n")
print("Exercício 2")
metros = float(input("Insira o número de metros: "))
print("%10.3f metros equivalem a %10.3f milímetros." %(metros, (metros * 1000)))
print("\n")


print("Exercício 3")
dias = int(input("Insira o número de dias: "))
horas = int(input("Insira o número de horas: "))
minutos = int(input("Insira o número de minutos: "))
segundos = int(input("Insira o número de segundos: "))
# Um minuto tem 60 segundos
# Uma hora tem 3600 (60 * 60) segundos
# Um dia tem 24 horas, logo 24 * 3600 segundos
total_em_segundos = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos
print("Convertido em segundos é igual a %10d segundos." %total_em_segundos)
print("Convertido em segundos é igual a %10d segundos." %((dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos))
print("Convertido em segundos é igual a %d segundos." %((dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos))
