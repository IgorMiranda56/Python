import os
precoProduto = []
def cabecalho():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def inflacionar(valor):
    preco = 0
    if produto < 100:
        preco10 = preco * 0.01
        precoTotal10 = preco - preco10 
    else:
        preco20 = preco * 0.02
    return 
produto = int(input("Digite o preço produto:"))
precoProduto.append(produto)

precoTotal = inflacionar(precoProduto)

print(f"Preço a pagar: {precoTotal}")