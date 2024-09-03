class Autor:
    def __init__(self, nome, nacionalidade, dataNascimento):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.dataNascimento = dataNascimento

    def nome(self):
        return self._nome

    
    def nome(self, nome):
        self._nome = nome

    def nacionalidade(self):
        return self._nacionalidade

    
    def nacionalidade(self, nacionalidade):
        self._nacionalidade = nacionalidade


    def dataNascimento(self):
        return self._data_nascimento


    def data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento


    def exibir_autor(self):
        print(f"Nome: {self.nome}")
        print(f"Nacionalidade: {self.nacionalidade}")
        print(f"Data de Nascimento: {self.data_nascimento}")

if __name__ == "__main__":
    
    autor = Autor("Machado de Assis", "Brasileiro", "1839-06-21")

    autor.exibir_autor()   

