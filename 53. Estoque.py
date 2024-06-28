import os
import time

def Menu():
    print("=== ESTOQUE ===")
    print("1 - Registrar produto.")
    print("2 - Consultar produto.")
    print("3 - Mostrar todos os produto.")
    print("4 - Remover produto.")
    print("5 - Sair")

def Consultar(estoque, opcaoProduto):
    for i in estoque:
        if opcaoProduto == i.codigo:
            print(f"Nome do produto: {i.nome}")
            print(f"Quantidade do produto: {i.quantidade}")
            print(f"Preco do produto: {i.preco}")
            return
        print("Produto não encontrado.")

def Deletar(estoque, excluir):
    for i in estoque:
        if excluir == i.codigo:
            estoque.remove(i)
            return
        print("Produto não encontrado.")

class Estoque():
    def __init__(self, codigoProduto: int, nomeProduto, quantidadeProduto: int, precoProduto: float):
        self.codigo = codigoProduto
        self.nome = nomeProduto
        self.quantidade = quantidadeProduto
        self.preco = precoProduto

vetorEstoque = []

while True:
    Menu()
    opcao = int(input("Digite uma das opções: "))
    match(opcao):
        case 1:
            codigoProduto = int(input("Digite o código do produto: "))
            nomeProduto = input("Digite o nome do produto: ")
            while True:
                quantidadeProduto = int(input("Digite a quantidade do produto: "))
                if quantidadeProduto < 0 or quantidadeProduto > 10:
                    print("Digite um valor maior que 0 ou menor que 10. ")
                    time.sleep(0.5)
                    os.system("cls || clear")
                else:
                    break
            while True:
                precoProduto = float(input("Digite o preço do produto: "))
                if precoProduto < 0.1:
                    print("Digite um valor maior que 0. ")
                    time.sleep(0.5)
                    os.system("cls || clear")
                else:
                    break
            vetorEstoque.append(Estoque(codigoProduto, nomeProduto, quantidadeProduto, precoProduto))

        case 2:
            opcaoProduto = int(input("Digite o código do produto que deseja consultar: "))
            os.system("cls || clear")
            Consultar(vetorEstoque, opcaoProduto)
            
        case 3:
            for i in vetorEstoque:
                print("=== Todos os produtos do estoque ===")
                print(f"Nome do produto: ", i.nome)
                print(f"Quantidade do produto: ", i.quantidade)
                print(f"Preço do produto: ", round(i.preco, 2))
                
        case 4:
            delete = int(input("Digite o código do produto que deseja excluir: "))
            Deletar(vetorEstoque, delete)
            os.system("cls || clear")

        case 5:
            print("Programa finalizado. ")
            break
        case _:
            os.system("cls || clear")
            print("Opção inválida. ")
            time.sleep(0.5)