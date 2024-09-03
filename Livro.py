from Autor import Autor

class Livro:
    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao

    def titulo(self):
        return self._titulo

    def titulo(self, titulo):
        self._titulo = titulo
 
    def autor(self):
        return self._autor

    def autor(self, autor):
        self._autor = autor

    def anoPublicacao(self):
        return self._ano_publicacao

    def anoPublicacao(self, ano_publicacao):
        self._ano_publicacao = ano_publicacao

    def exibir_livro(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor.nome}")
        print(f"Ano de Publicação: {self.anoPublicacao}")

if __name__ == "__main__":
    
    autor = Autor("Machado de Assis", "Brasileiro", "1839-06-21")

    livro = Livro("Dom Casmurro", autor, 1899)

    livro.exibir_livro()    
