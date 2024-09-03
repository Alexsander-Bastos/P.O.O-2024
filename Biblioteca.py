from Livro import Livro
from Autor import Autor

class Biblioteca:
     def __init__(self):
        self.livros = []

     def adicionar_livro(self, livro):
        if isinstance(livro, Livro):
            self.livros.append(livro)
        else:
            print("O objeto não é um livro válido.")

     def exibir_livros(self):
        if not self.livros:
            print("Nenhum livro na biblioteca.")
        for livro in self.livros:
            livro.exibir_livro()
            print()

if __name__ == "__main__":
    
    autor = Autor("Machado de Assis", "Brasileiro", "1839-06-21")

    livro1 = Livro("Dom Casmurro", autor, 1899)
    livro2 = Livro("Memórias Póstumas de Brás Cubas", autor, 1881)

    biblioteca = Biblioteca()

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    biblioteca.exibir_livros()