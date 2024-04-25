# Porcentagem

import os

os.system("cls || clear")

nome = str(input("Digite o nome do produto: "))
produto = int(input("Digite 1 para Maçã ou 2 para Morango: "))
quantidade = int(input("Digite a quantidade (em quilos) do produto: "))

precoMaca = 2.50
precoMorango = 1.50

if quantidade <= 5 and produto == 1:
    total = quantidade * 2.5
    totalDesconto = (total * 0.02) - total
elif quantidade > 5 and produto == 1:
    total = quantidade * 2.2
    totalDesconto = (total * 0.04) - total
elif quantidade <= 5 and produto == 2:
    total = quantidade * 1.5
    totalDesconto = (total * 0.03) - total 
elif quantidade > 5 and produto == 2:
    total = quantidade * precoMorango
    totalDesconto = (total * 0.05) - total

print(f"Nome do produto: {nome}")
print(f"Quantidade do produto: {quantidade}")
print(f"Preço a pagar: R${totalPagar}")