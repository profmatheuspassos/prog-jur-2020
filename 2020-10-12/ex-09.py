n = int(input("Tabuada de: "))
inicio = int(input("De: "))
fim = int(input("Até: "))
x = inicio
while inicio <= fim:
    print("%d x %d = %d" %(n, inicio, n*inicio))
    inicio = inicio + 1
