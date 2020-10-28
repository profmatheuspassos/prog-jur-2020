print("\nJogos Olímpicos\nPrograma oficial para cálculo de notas\nCategoria: Patinação no Gelo")
while True:
    # Vejam que neste programa não será feita nenhuma comparação. Em vez disso, será necessário mostrar a análise de um único atleta por vez.
    # É por este motivo que esta variável é inicializada dentro do while, e não fora.
    nomeAtleta = input("\nDigite o nome do atleta ou \"fim\" para encerrar o programa: ")
    if nomeAtleta == "fim": # Mecanismo de controle para sair do while
        break

    # Aqui temos vários blocos while que fazem a mesma coisa: verificam se o que a pessoa inseriu é ou não um número
    # pelo menos igual a zero ou positivo (pois não existem notas negativas nas Olimpíadas)
    while True:
        nota1 = input("Insira a nota do jurado 1 com \".\" para números decimais, se for o caso: ")
        try:
            nota1 = float(nota1)
        except:
            print("Por favor, digite apenas números com \".\" para números decimais, se for o caso.")
            continue
        if nota1 < 0:
            print("Não existe nota negativa nas Olimpíadas.")
            continue
        break
    while True:
        nota2 = input("Insira a nota do jurado 2 com \".\" para números decimais, se for o caso: ")
        try:
            nota2 = float(nota2)
        except:
            print("Por favor, digite apenas números com \".\" para números decimais, se for o caso.")
            continue
        if nota2 < 0:
            print("Não existe nota negativa nas Olimpíadas.")
            continue
        break
    while True:
        nota3 = input("Insira a nota do jurado 3 com \".\" para números decimais, se for o caso: ")
        try:
            nota3 = float(nota3)
        except:
            print("Por favor, digite apenas números com \".\" para números decimais, se for o caso.")
            continue
        if nota3 < 0:
            print("Não existe nota negativa nas Olimpíadas.")
            continue
        break
    while True:
        nota4 = input("Insira a nota do jurado 4 com \".\" para números decimais, se for o caso: ")
        try:
            nota4 = float(nota4)
        except:
            print("Por favor, digite apenas números com \".\" para números decimais, se for o caso.")
            continue
        if nota4 < 0:
            print("Não existe nota negativa nas Olimpíadas.")
            continue
        break
    while True:
        nota5 = input("Insira a nota do jurado 5 com \".\" para números decimais, se for o caso: ")
        try:
            nota5 = float(nota5)
        except:
            print("Por favor, digite apenas números com \".\" para números decimais, se for o caso.")
            continue
        if nota5 < 0:
            print("Não existe nota negativa nas Olimpíadas.")
            continue
        break

    # Abaixo é feita a atribuição da maior e da menor nota, já que o critério irá excluí-las da média do atleta
    if nota1 > nota2 and nota1 > nota3 and nota1 > nota4 and nota1 > nota5:
        maiorNota = nota1
    elif nota2 > nota3 and nota2 > nota4 and nota2 > nota5:
        maiorNota = nota2
    elif nota3 > nota4 and nota3 > nota5:
        maiorNota = nota3
    elif nota4 > nota5:
        maiorNota = nota4
    else:
        maiorNota = nota5
    if nota1 < nota2 and nota1 < nota3 and nota1 < nota4 and nota1 < nota5:
        menorNota = nota1
    elif nota2 < nota3 and nota2 < nota4 and nota2 < nota5:
        menorNota = nota2
    elif nota3 < nota4 and nota3 < nota5:
        menorNota = nota3
    elif nota4 < nota5:
        menorNota = nota4
    else:
        menorNota = nota5

    # A média do atleta será calculada somando-se todas as suas notas menos a menor e a maior, e tudo isto dividido por 3
    mediaNota = (nota1 + nota2 + nota3 + nota4 + nota5 - maiorNota - menorNota) / 3
    print("\nNome do atleta: " + nomeAtleta + ".")
    print("Maior nota: " + str(maiorNota) + ".")
    print("Menor nota: " + str(menorNota) + ".")
    print("Média de notas: " + str(mediaNota) + ".\n")
print("\nObrigado por utilizar nosso programa. Até a próxima Olimpíada :)\n")
