from Produto import Produto
from typing import List

class Venda:
    def __init__(self, produtos: List[Produto], dataVenda: str):
        self._produtos = produtos
        self._dataVenda = dataVenda
        self._total = self.calcular_total()

    def produtos(self):
        return self._produtos

    def produtos(self, produtos: List[Produto]):
        if not all(isinstance(p, Produto) for p in produtos):
            raise ValueError("Todos os itens devem ser objetos da classe Produto.")
        self._produtos = produtos
        self._total = self.calcular_total()
    def dataVenda(self):
        return self._dataVenda

    def dataVenda(self, dataVenda: str):
        self._dataVenda = dataVenda

    def total(self):
        return self._total

    def calcular_total(self) -> float:
        return sum(produto.preco for produto in self._produtos)

    def exibir_venda(self):
        print(f"Data da Venda: {self.dataVenda}")
        print(f"Total: R${self.total:.2f}")
        print("Produtos:")
        for produto in self._produtos:
            produto.exibir_produto()
            print()

if __name__ == "__main__":
    produto1 = Produto("Camiseta", 29.90, 100)
    produto2 = Produto("Calça", 89.90, 50)

    lista_produtos = [produto1, produto2]

    venda = Venda(lista_produtos, "2024-09-01")

    venda.exibir_venda()