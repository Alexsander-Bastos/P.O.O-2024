from Autor import Autor
from Livro import Livro
from Biblioteca import Biblioteca

def menu():
    print("Menu da Biblioteca")
    print("1. Adicionar Livro")
    print("2. Remover Livro")
    print("3. Buscar Livro")
    print("4. Listar Todos os Livros")
    print("5. Sair")

def main():
    biblioteca = Biblioteca()

    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Título do livro: ")
            autor_nome = input("Nome do autor: ")
            ano_publicacao = int(input("Ano de publicação: "))
            autor = Autor(autor_nome, "Desconhecido", "Desconhecida")
            livro = Livro(titulo, autor, ano_publicacao)
            biblioteca.adicionar_livro(livro)

        elif escolha == '2':
            titulo = input("Título do livro a ser removido: ")
            biblioteca.remover_livro(titulo)

        elif escolha == '3':
            titulo = input("Título do livro a ser buscado: ")
            biblioteca.buscar_livro(titulo)

        elif escolha == '4':
            biblioteca.listar_livros()

        elif escolha == '5':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida, por favor escolha novamente.")

if __name__ == "__main__":
    main()