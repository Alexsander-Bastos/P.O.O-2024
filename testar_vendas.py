from Produto import Produto
from Venda import Venda

def menu():
    print("Menu de Vendas")
    print("1. Adicionar Produto à Venda")
    print("2. Remover Produto da Venda")
    print("3. Listar Todos os Produtos da Venda")
    print("4. Mostrar Total da Venda")
    print("5. Sair")

def main():
    produtos = []
    venda = Venda(produtos, "2024-09-01")  

    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            produto = Produto(nome, preco, quantidade)
            produtos.append(produto)
            venda.produtos = produtos
            print(f"Produto '{nome}' adicionado à venda.")

        elif escolha == '2':
            nome = input("Nome do produto a ser removido: ")
            produtos = [p for p in produtos if p.nome.lower() != nome.lower()]
            venda.produtos = produtos
            print(f"Produto '{nome}' removido da venda.")

        elif escolha == '3':
            if not venda.produtos:
                print("Nenhum produto na venda.")
            else:
                print("Produtos na venda:")
                venda.exibir_venda()

        elif escolha == '4':
            print(f"Total da venda: R${venda.calcular_total():.2f}")

        elif escolha == '5':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida, por favor escolha novamente.")

if __name__ == "__main__":
    main()