from Conta_Bancaria import Conta_bancaria
from Conta_Corrente import Conta_corrente
from Conta_Poupança import Conta_poupança

def criar_conta_corrente():
    titular = input("Digite o nome do titular: ")
    cpf = input("Digite o CPF do titular: ")
    numerocc = input("Digite o número da conta corrente: ")
    saldo = float(input("Digite o saldo inicial: "))
    return Conta_corrente(titular, cpf, numerocc, saldo)

def criar_conta_poupanca():
    titular = input("Digite o nome do titular: ")
    cpf = input("Digite o CPF do titular: ")
    rendimento = float(input("Digite a taxa de rendimento (%): "))
    saldo = float(input("Digite o saldo inicial: "))
    return Conta_poupança(titular, cpf, rendimento, saldo)

def menu():
    contas = {}
    while True:
        print("\nMenu:")
        print("1. Criar conta corrente")
        print("2. Criar conta poupança")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Verificar saldo")
        print("6. Mostrar informações da conta")
        print("7. Ver rendimento da conta poupança")
        print("8. Aplicar rendimento na conta poupança")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            conta = criar_conta_corrente()
            contas[conta.cpf] = conta
            print("Conta corrente criada com sucesso!")

        elif opcao == '2':
            conta = criar_conta_poupanca()
            contas[conta.cpf] = conta
            print("Conta poupança criada com sucesso!")

        elif opcao == '3':
            cpf = input("Digite o CPF da conta: ")
            if cpf in contas:
                valor = float(input("Digite o valor a ser depositado: "))
                contas[cpf].depositar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == '4':
            cpf = input("Digite o CPF da conta: ")
            if cpf in contas:
                valor = float(input("Digite o valor a ser sacado: "))
                contas[cpf].sacar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == '5':
            cpf = input("Digite o CPF da conta: ")
            if cpf in contas:
                contas[cpf].verificar_saldo()
            else:
                print("Conta não encontrada.")

        elif opcao == '6':
            cpf = input("Digite o CPF da conta: ")
            if cpf in contas:
                if isinstance(contas[cpf], Conta_corrente):
                    contas[cpf].mostrarcc()
                elif isinstance(contas[cpf], Conta_poupança):
                    contas[cpf].mostrar_conta()
                    contas[cpf].ver_rendimento()
            else:
                print("Conta não encontrada.")

        elif opcao == '7':
            cpf = input("Digite o CPF da conta poupança: ")
            if cpf in contas and isinstance(contas[cpf], Conta_poupança):
                contas[cpf].ver_rendimento()
            else:
                print("Conta poupança não encontrada.")

        elif opcao == '8':
            cpf = input("Digite o CPF da conta poupança: ")
            if cpf in contas and isinstance(contas[cpf], Conta_poupança):
                contas[cpf].render()
            else:
                print("Conta poupança não encontrada.")

        elif opcao == '9':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()