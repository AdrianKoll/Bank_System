menu = """
============ SISTEMA BANCARIO ============

\033[1;36m[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair\033[0m

Digite a opção desejada: """

# Inicialização de variáveis
saldo = 0.0
limite = 500.0
extrato = []
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    # Depósito
    if opcao == "1":
        try:
            deposito = float(input("Digite a quantidade de dinheiro que gostaria de depositar: R$ "))
            if deposito > 0:
                saldo += deposito
                extrato.append(f"\033[32mDepósito: R$ {deposito:.2f}\033[0m")
                print(f"Depósito realizado com sucesso! \033[34mSaldo atual: R$ {saldo:.2f}\033[0m")
            else:
                print("O valor do depósito deve ser maior que zero.")
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

    # Saque
    elif opcao == "2":
        try:
            saque = float(input("Digite a quantidade de dinheiro que gostaria de sacar: R$ "))
            if 0 < saque <= saldo and numero_saques < LIMITE_SAQUE and saque <= limite:
                saldo -= saque
                numero_saques += 1
                extrato.append(f"\033[31mSaque: R$ {saque:.2f}\033[0m")
                print(f"Saque realizado com sucesso! \033[34mSaldo atual: R$ {saldo:.2f}\033[0m")
            elif saque > limite:
                print(f"limite de R${limite:.2f} por saque")
            elif numero_saques >= LIMITE_SAQUE:
                print("Limite de saques diários atingido.")
            elif saque < 0:
                print("O valor do saque deve ser maior que 0")
            else:
                print("Saldo insuficiente.")
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

    # Extrato
    elif opcao == "3":
        print(f"\n============ EXTRATO ============\n")
        if extrato:
            for operacao in extrato:
                print(operacao)
        else:
            print("Não há movimentações.")
        print(f"\033[34mSaldo atual: R$ {saldo:.2f}\033[0m")

    # Sair
    elif opcao == "4":
        print("Obrigado por utilizar o sistema bancário!")
        break

    else:
        print("Opção inválida, por favor selecione novamente.")