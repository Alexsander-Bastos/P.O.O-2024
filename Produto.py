class Produto:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def preco(self):
        return self._preco

    def preco(self, preco):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = preco

    def quantidade(self):
        return self._quantidade

    def quantidade(self, quantidade):
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        self._quantidade = quantidade

    def exibir_produto(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")

if __name__ == "__main__":
    produto = Produto("Camiseta", 29.90, 100)

    produto.exibir_produto()

    produto.preco = 25.00
    produto.quantidade = 150

    produto.exibir_produto()