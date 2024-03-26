menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 1500
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Por favor, insira o valor a depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação não realizada. Verifique as informações e tente novamente!")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação não realizada. Você não possui saldo suficiente. Verifique as informaçõese tente novamente.")

        elif excedeu_limite:
            print("Operação não realizada. Valor maior que o limite. Verifique as informações e tente novamente.")

        elif excedeu_saques:
            print("Operação não realizada. Quantidade de saques limite atingida. Tente novamente amanhã!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou! Valor informado inválido.")

      
    elif opcao == "3":

        print("\n===================EXTRATO===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================================")
        

    elif opcao == "0":
        print("Saindo do programa. Obrigado por usar nossos serviços!")
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
        