import os
precoProduto = []
def cabecalho():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def inflacionar(valor):
    if preco < 100:
        desconto10 = preco * 0.01
        precoTotal10 = preco - desconto10 
    else:
        desconto20 = preco * 0.02
        precoTotal20 = preco - desconto20
    return precoTotal

preco = int(input("Digite o preço produto:"))

precoTotal = inflacionar(precoProduto)

print(f"Preço a pagar: {precoTotal}")