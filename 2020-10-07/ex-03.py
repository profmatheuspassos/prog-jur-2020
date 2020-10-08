velocidade = float(input("Digite a velocidade do seu carro: "))
if velocidade > 80:
#    multa = (velocidade - 80) * 5
#    print("Você foi multado em € %.2f!" %multa)
    print("Você foi multado em € %.2f!" %((velocidade - 80) * 5))
if velocidade <= 80:
    print("Sua velocidade está ok, boa viagem!")
