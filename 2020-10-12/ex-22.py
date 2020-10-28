# Para resolver este problema podemos usar strings.
# Veja que estamos lendo o número sem convertê-lo para int ou float: desta forma o valor de s será uma string
num_string = input("Digite o número a verificar, sem espaços: ")
inicio = 0
fim = len(num_string) - 1 # posição do último caracter da string
while fim > inicio and num_string[inicio] == num_string[fim]:
    fim = fim - 1
    inicio = inicio + 1
if num_string[inicio] == num_string[fim]:
    print("%s é palíndromo." %num_string)
else:
    print("%s não é palíndromo." %num_string)
