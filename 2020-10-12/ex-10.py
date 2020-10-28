valores = 0
questao = 1
while questao <= 3:
    resposta = input("Resposta da questão %d: " %questao)
    if questao == 1 and resposta == "b":
        valores = valores + 1
    if questao == 2 and resposta == "a":
        valores = valores + 1
    if questao == 3 and resposta == "d":
        valores = valores + 1
    questao += 1
print("O aluno fez %d valor(es)." %valores)
