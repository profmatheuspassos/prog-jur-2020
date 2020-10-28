# Inicialização de variáveis
totalClientes = totalAltura = numHomens = numMulheres = 0
maisAlto = maisBaixo = None
while True:
    codCliente = input("\nDigite o código do cliente ou \"0\" para encerrar o programa: ")
    try:
        codCliente = int(codCliente)
    except: # Se a pessoa não inserir um número, retorna para o início do while
        print("\nPor favor, digite apenas números como código do cliente.")
        continue
    if codCliente == 0: # Se a pessoa inseriu zero, sai do while
        break
    if codCliente < 0: # Se a pessoa inseriu um código negativo, exibe a mensagem e volta para o início do while
        print("\nCódigos de cliente não podem ser negativos. Insira um código de cliente válido ou \"0\" para encerrar o programa.")
        continue
    totalClientes += 1 # Se tudo deu certo até aqui, aumenta em 1 o contador do total de clientes para o cálculo final

    # Aqui optei por criar um novo while para controlar se a pessoa está inserindo as letras M, F ou alguma outra letra
    while True:
        sexoCliente = input("\nDigite o sexo do cliente (M ou F): ")

        # Abaixo uma novidade: utilizei o método .upper() para converter o que a pessoa inseriu em letras maiúsculas
        # O objetivo é fazer a comparação do if/else a seguir sem me preocupar se a pessoa inseriu M ou m, por exemplo
        sexoCliente = sexoCliente.upper()
        if sexoCliente == "M":
            numHomens += 1
        elif sexoCliente == "F":
            numMulheres += 1
        else: # Se a pessoa inseriu outra letra que não M ou F, volta para o início deste while (e não do while geral)
            print("\nPor favor, digite apenas \"M\" ou \"F\".")
            continue
        break # A função deste break é sair do while que controla a entrada de M ou F

    # Abaixo o mesmo raciocínio do while acima: controlar se as pessoas estão inserindo apenas números na altura dos clientes
    while True:
        alturaCliente = input("\nDigite a altura do cliente usando \".\" para indicar casas decimais: ")
        try:
            alturaCliente = float(alturaCliente)
        except:
            print("\nPor favor, digite apenas números com \".\" para indicar casas decimais.")
            continue
        break

    # Ao final preciso calcular a média dos clientes - portanto, ao valor da altura total será adicionada a altura do cliente atual
    totalAltura += alturaCliente

    # Definição das informações referentes aos clientes mais altos e mais baixos
    if maisAlto == None or alturaCliente > maisAlto:
        maisAlto = alturaCliente
        codClienteMaisAlto = codCliente
        sexoClienteMaisAlto = sexoCliente
    if maisBaixo == None or alturaCliente < maisBaixo:
        maisBaixo = alturaCliente
        codClienteMaisBaixo = codCliente
        sexoClienteMaisBaixo = sexoCliente

# Este try é necessário porque o utilizador pode ter inserido o número zero já na primeira execução do programa
# Se não houvesse este try daria erro no programa
try:
    mediaAltura = totalAltura / totalClientes
    print("\nCódigo do cliente mais alto: " + str(codClienteMaisAlto) + ".")
    print("Sexo do cliente mais alto: " + sexoClienteMaisAlto + ".")
    print("Altura do cliente mais alto: " + str(maisAlto) + ".")
    print("\nCódigo do cliente mais baixo: " + str(codClienteMaisBaixo) + ".")
    print("Sexo do cliente mais baixo: " + sexoClienteMaisBaixo + ".")
    print("Altura do cliente mais baixo: " + str(maisBaixo) + ".")
    print("\nMédia de altura dos clientes: " + str(mediaAltura) + ".\n")
    if numHomens > numMulheres:
        print("Há mais clientes homens do que clientes mulheres.\n")
    elif numHomens < numMulheres:
        print("Há mais clientes mulheres do que clientes homens.\n")
    else:
        print("Há um número igual de clientes homens e clientes mulheres.\n")
except:
    print("\nVocê não inseriu nenhuma informação. Portanto, não tenho como apresentar nenhum resultado válido. Até a próxima :)\n")
