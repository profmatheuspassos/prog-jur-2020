# Inicialização de variáveis e exibição e mensagens iniciais
numTotalAlunos = notaTotalTurma = 0
notaMaisAlta = notaMaisBaixa = None
print("\nProgramação para Juristas - FDUNL")
print("Professor Matheus Silva")
print("\nCritérios de avaliação:")
print("\n1) O programa funciona sem erros (12 valores)")
print("2) Apresentação dos resultados (2 valores)")
print("3) Número de linhas do código (3 valores)")
print("4) Criatividade do código e de sua execução (3 valores)")
while True:
    numAluno = input("\nInsira o número do aluno ou \"9999\" para encerrar o programa: ")

    # Block try...except para testar se foram inseridos números
    try:
        numAluno = int(numAluno)
    except:
        print("Por favor, insira apenas números. Tente novamente.")
        continue

    # Dois if's para verificar se foi inserido o código para encerrar o programa ou se foram inseridos números negativos
    if numAluno == 9999:
        break
    if numAluno < 0:
        print("\nNão existem números de aluno negativos ;) Por favor, insira o número do aluno de maneira correta.")
        continue

    # Se tudo deu certo, soma-se 1 ao número total de alunos
    numTotalAlunos += 1

    # O bloco while abaixo tem por objetivo testar se a pessoa está inserindo apenas números nos critérios de avaliação
    # A lógica é exatamente a mesma para os quatro blocos while: 1) Testa se foi inserido número; 2) Verifica-se se foram inseridos
    # valores que correspondem ao mínimo e máximo permitido para cada critério; 3) Se tudo estiver ok, soma o número inserido
    # à nota total do aluno; 4) Sai do while atual e passa para o próximo.
    while True:
        notaTotalAluno = 0
        notaCriterio1 = input("Insira o valor atribuído ao critério 1 utilizando \".\" para números decimais, se for o caso: ")
        try:
            notaCriterio1 = float(notaCriterio1)
        except:
            print("Por favor, insira apenas números utilizando \".\" para números decimais, se for o caso.")
            continue
        if notaCriterio1 < 0 or notaCriterio1 > 12:
            print("Insira apenas números entre 0 e 12, por favor.")
            continue
        notaTotalAluno += notaCriterio1
        break
    while True:
        notaCriterio2 = input("Insira o valor atribuído ao critério 2 utilizando \".\" para números decimais, se for o caso: ")
        try:
            notaCriterio2 = float(notaCriterio2)
        except:
            print("Por favor, insira apenas números utilizando \".\" para números decimais, se for o caso.")
            continue
        if notaCriterio2 < 0 or notaCriterio2 > 2:
            print("Insira apenas números entre 0 e 2, por favor.")
            continue
        notaTotalAluno += notaCriterio2
        break
    while True:
        notaCriterio3 = input("Insira o valor atribuído ao critério 3 utilizando \".\" para números decimais, se for o caso: ")
        try:
            notaCriterio3 = float(notaCriterio3)
        except:
            print("Por favor, insira apenas números utilizando \".\" para números decimais, se for o caso.")
            continue
        if notaCriterio3 < 0 or notaCriterio3 > 3:
            print("Insira apenas números entre 0 e 3, por favor.")
            continue
        notaTotalAluno += notaCriterio3
        break
    while True:
        notaCriterio4 = input("Insira o valor atribuído ao critério 4 utilizando \".\" para números decimais, se for o caso: ")
        try:
            notaCriterio4 = float(notaCriterio4)
        except:
            print("Por favor, insira apenas números utilizando \".\" para números decimais, se for o caso.")
            continue
        if notaCriterio4 < 0 or notaCriterio4 > 3:
            print("Insira apenas números entre 0 e 3, por favor.")
            continue
        notaTotalAluno += notaCriterio4
        break

    # Adiciona a nota total deste aluno à nota total da turma
    notaTotalTurma += notaTotalAluno

    # Faz comparações para verificar a nota mais alta e a nota mais baixa da turma
    if notaMaisAlta == None or notaTotalAluno > notaMaisAlta:
        notaMaisAlta = notaTotalAluno
        codNotaMaisAlta = numAluno
    if notaMaisBaixa == None or notaTotalAluno < notaMaisBaixa:
        notaMaisBaixa = notaTotalAluno
        codNotaMaisBaixa = numAluno

# O bloco try...except abaixo tem por objetivo verificar se lá no início a pessoa inseriu ou não o valor zero, encerrando o programa na primeira execução
try:
    mediaTurma = notaTotalTurma / numTotalAlunos
    print("\nNúmero total de alunos avaliados: " + str(numTotalAlunos) + ".")
    print("\nNúmero do aluno com nota mais alta: " + str(codNotaMaisAlta) + ".")
    print("Nota do aluno com nota mais alta: " + str(notaMaisAlta) + ".")
    print("\nNúmero do aluno com nota mais baixa: " + str(codNotaMaisBaixa) + ".")
    print("Nota do aluno com nota mais baixa: " + str(notaMaisBaixa) + ".")
    print("\nMédia das notas da turma: " + str(mediaTurma) + ".\n")
except:
    print("\nVocê não inseriu nenhuma nota, não me sendo possível indicar os resultados esperados. Obrigado e volte sempre!\n")
