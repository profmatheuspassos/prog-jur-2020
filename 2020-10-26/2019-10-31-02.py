# Inicialização de variáveis
totalVotos = votosJoao = votosMaria = votosJose = votosMargarida = votosBranco = votosNulo = 0
print("Urna eletrônica\n")
print("Abaixo o código do candidato e seu respectivo nome:\n")
print("1 - João")
print("2 - Maria")
print("3 - José")
print("4 - Margarida")
print("5 - Voto em branco")
print("6 - Voto nulo\n")
while True: # Execução por número de vezes indefinida
    try:
        opcaoEleitor = int(input("Digite o código escolhido conforme acima indicado ou \"0\" para encerrar a votação: "))
    except: # Se não inserir um número, mostra a mensagem abaixo e retorna para o início do while com o continue
        print("\nPor favor, insira apenas o número correspondente ao código da opção escolhida.\n")
        continue
    if opcaoEleitor == 0: # Se for inserido o número 0 sai do while
        break

    # Contagem do número de votos conforme as opções dos eleitores
    if opcaoEleitor == 1:
        votosJoao += 1
    elif opcaoEleitor == 2:
        votosMaria += 1
    elif opcaoEleitor == 3:
        votosJose += 1
    elif opcaoEleitor == 4:
        votosMargarida += 1
    elif opcaoEleitor == 5:
        votosBranco += 1
    elif opcaoEleitor == 6:
        votosNulo += 1
    else: # Se for inserido um valor que esteja fora dos códigos aceitos exibe a mensagem abaixo e volta para o início do while
        print("\nPor favor, insira apenas um dos códigos acima apresentados ou \"0\" para encerrar a votação.\n")
        continue

    # Se tudo der certo, soma-se 1 ao número total de votos para posterior cálculo das porcentagens
    totalVotos += 1

# Se houver votos, mostram-se estas mensagens
if totalVotos > 0:
    print("\nTotal de votos: " + str(totalVotos) + ".\n")
    print("Total de votos do João: " + str(votosJoao) + ".")
    print("Porcentagem de votos do João: " + str(int(((votosJoao / totalVotos) * 100))) + "%.\n")
    print("Total de votos da Maria: " + str(votosMaria) + ".")
    print("Porcentagem de votos da Maria: " + str(int(((votosMaria / totalVotos) * 100))) + "%.\n")
    print("Total de votos do José: " + str(votosJose) + ".")
    print("Porcentagem de votos do José: " + str(int(((votosJose / totalVotos) * 100))) + "%.\n")
    print("Total de votos da Margarida: " + str(votosMargarida) + ".")
    print("Porcentagem de votos da Margarida: " + str(int(((votosMargarida / totalVotos) * 100))) + "%.\n")
    print("Total de votos em branco: " + str(votosBranco) + ".")
    print("Porcentagem de votos em branco: " + str(int(((votosBranco / totalVotos) * 100))) + "%.\n")
    print("Total de votos nulos: " + str(votosNulo) + ".")
    print("Porcentagem de votos nulos: " + str(int(((votosNulo / totalVotos) * 100))) + "%.\n")

# Mensagem a ser exibida caso tenha sido inserido o número zero já na primeira execução do programa
else:
    print("\nVocê não votou em ninguém. Sou uma urna eletrônica inútil :\'(")
