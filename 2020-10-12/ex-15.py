deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (ex.: 3 para 3%): "))
investimento = float(input("Depósito mensal: "))
mes = 1
saldo = deposito
while mes <= 24:
    saldo = saldo + (saldo * (taxa / 100)) + investimento
    print ("O saldo do mês %d é de € %.2f." %(mes, saldo))
    mes = mes + 1
print ("O ganho obtido com os juros foi de € %.2f." %(saldo - deposito))
