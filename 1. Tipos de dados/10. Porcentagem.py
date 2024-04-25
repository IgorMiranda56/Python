# Porcentagem

import os

os.system("cls || clear")
produto = 0
quantidade = 0

nome = str(input("Digite o nome do produto: "))
preco = int(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

if quantidade <= 5:
    desconto = 0.02
elif quantidade <= 10:
    desconto = 0.03
else:
    desconto = 0.05

subTotal = preco * quantidade
totalPagar = subTotal - (subTotal * desconto)

print(f"Nome do produto: {nome}")
print(f"Quantidade do produto: {quantidade}")
print(f"Preço a pagar: R${totalPagar}")