class Conta_bancaria:
    def __init__(self, titular, cpf, saldo=0.0):
        self.titular = titular
        self.cpf = cpf
        self.saldo = saldo

    def mostrar_conta(self):
        print(f"Titular: {self.titular}")
        print(f"CPF: {self.cpf}")
        print(f"Saldo: R${self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")