# Inicializa variáveis
idadeZeroVinte = idadeVinteUmQuarenta = idadeQuarentaUmSessenta = idadeSessentaUmOitenta = idadeMaisOitenta = numTotalPessoas = somaTotalIdade = 0

# Executa o código de maneira ininterrupta:
while True:
    try:
        idade = int(input("Digite a idade do aluno ou \"-1\" para encerrar: "))

    # Se a pessoa digitar letras ou números com casas decimais é mostrada esta singela mensagem:
    except:
        print("Digite apenas números inteiros, por favor ;)\n")
        continue # Aqui o programa volta para o início do while

    # Se for inserido -1 o programa sai do while:
    if idade == -1:
        break

    # Se for inserida idade maior que 100 anos é mostrada uma mensagem carinhosa:
    if idade > 100:
        print("Será mesmo uma pessoa tão velhinha assim? A idade máxima para mim é de 100 anos :)\n")
        continue

    # Contadores para cada uma das idades que importam no programa:
    elif idade > 80:
        idadeMaisOitenta += 1
    elif idade > 60:
        idadeSessentaUmOitenta += 1
    elif idade > 40:
        idadeQuarentaUmSessenta += 1
    elif idade > 20:
        idadeVinteUmQuarenta += 1
    elif idade >= 0:
        idadeZeroVinte += 1

    # E se alguém inserir uma idade negativa que não seja -1?
    else:
        print("Ninguém tem idade negativa, não é mesmo? :)\n")
        continue # Retorna para o início do while

    numTotalPessoas += 1 # Somatório do número total de pessoas
    somaTotalIdade += idade # Somatório das idades totais para posterior cálculo da média

try:
    mediaIdade = int(somaTotalIdade / numTotalPessoas)
    print("\nNúmero total de pessoas analisadas: " + str(numTotalPessoas) + ".\n")
    print("Número de pessoas com idade inferior a 20 anos: " + str(idadeZeroVinte) + ".")
    print("Número de pessoas com idade entre 21 e 40 anos: " + str(idadeVinteUmQuarenta) + ".")
    print("Número de pessoas com idade entre 41 e 60 anos: " + str(idadeQuarentaUmSessenta) + ".")
    print("Número de pessoas com idade entre 61 e 80 anos: " + str(idadeSessentaUmOitenta) + ".")
    print("Número de pessoas com idade superior a 80 anos: " + str(idadeMaisOitenta) + "\n")
    if mediaIdade > 61:
        print("A maioria das pessoas é idosa (idade média acima de 60 anos).")
    elif mediaIdade > 26:
        print("A maioria das pessoas é adulta (idade média entre 26 e 60 anos).")
    else:
        print("A maioria das pessoas é jovem (idade média até 25 anos).")

# A mensagem abaixo é exibida se a pessoa executar o programa e já digitar "-1" logo na primeira vez
except:
    print("\nSem você ter inserido idades sou inútil :( Execute-me novamente!\n")
