import os

def conversor_nota(a):
    if a > 1:
        print("O número deve ser entre 0.0 e 1.0!")
    elif a < 0:
        print("O número deve ser entre 0.0 e 1.0!")
    elif a >= 0.9:
        print("Superior")
    elif a >= 0.8:
        print("Médio superior")
    elif a >= 0.7:
        print("Médio")
    elif a >= 0.6:
        print("Médio inferior")
    else:
        print("Insuficiente")

def limpa_tudo():
    print("Aperte \"enter\" para continuar...")
    input()
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    while True:
        nota = input("Digite a sua nota com valores entre 0.0 e 1.0 ou \"-1\" para encerrar: ")
        try:
            nota = float(nota)
            break
        except:
            print("Por favor, digite apenas números com pontos para indicar decimais, se for o caso.")
            limpa_tudo()
            continue
    if nota == -1:
        print("Obrigado por utilizar o programa.")
        limpa_tudo()
        break
    conversor_nota(nota)
    limpa_tudo()
