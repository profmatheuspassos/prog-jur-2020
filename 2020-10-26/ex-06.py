def sequencia(n):
    print("\n")
    for num in range(1, n + 1):
        for i in range(num):
            print (num, end=" ")
        print("\n")
num = int(input("Digite um número: "))
if num < 1 or num > 9:
    print("O número tem de ser entre 1 e 9. Tente novamente.")
else:
    sequencia(num)
