from Conta_Bancaria import Conta_bancaria

class Conta_poupança:
    def __init__(self, titular, CPF, saldo, rendimento):
        super().__init__(titular, CPF, saldo)
        self.rendimento = rendimento

    def ver_rendimento(self):
        print(f"Taxa de rendimento: {self.rendimento*100: .2f}% ao ano")

    def render(self):
        rendimento_aplicado = self.saldo * self.rendimento
        self.saldo += rendimento_aplicado
        print(f"Rendimento aplicado: R${rendimento_aplicado: .2f}")   