import os

def cabecalho():
    os.system("cls || clear")
    print("=== SENAI ===")

class Livro:
    def __init__(self, nomeTitulo, nomeAutor, numeroPaginas: int, precoLivro: float):
        self.titulo = nomeTitulo
        self.autor = nomeAutor
        self.paginas = numeroPaginas
        self.preco = precoLivro

QUANTIDADE = 2
livros = []

cabecalho()
for i in range(QUANTIDADE):
    nomeTitulo = input("Digite o nome do livro: ")
    nomeAutor = input("Digite o nome do autor: ")
    numeroPagina = int(input("Digite o número de páginas: "))
    precoLivro = float(input("Digite o preço do livro: "))
    livros.append(Livro(nomeTitulo, nomeAutor, numeroPagina, precoLivro))

cabecalho()
for i in livros:
    print(f"Titulo: {i.titulo}")
    print(f"Autor: {i.autor}")
    print(f"Número de páginas: {i.paginas}")
    print(f"Preço do livro: {i.preco}")
