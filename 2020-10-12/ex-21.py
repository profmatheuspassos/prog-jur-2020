n = int(input("Digite um número: "))
if n < 0:
    print("Número inválido. Digite apenas valores positivos.")
if n == 0 or n == 1:
    print("%d é um caso especial." %n)
else:
    if n == 2:
        print("2 é primo.")
    elif n % 2 == 0:
        print("%d não é primo, pois 2 é o único número par primo." %n)
    else:
        x = 3
        while(x < n):
            if n % x == 0:
                break
            x = x + 2
        if x == n:
            print("%d é primo." %n)
        else:
            print("%d não é primo, pois é divisível por %d." %(n, x))
