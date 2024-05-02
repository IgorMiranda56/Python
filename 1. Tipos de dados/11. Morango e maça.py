# Porcentagem

import os

os.system("cls || clear")

pesoMaca = float(input("Digite a quantidade de maçã (em quilos) do produto: "))
pesoMorango = float(input("Digite a quantidade de morango (em quilos) do produto: "))

if pesoMaca < 5:
    precoMaca = 1.80
else:
    precoMaca = 1.50
if pesoMorango < 5:
    precoMorango = 2.50
else:
    precoMorango = 2.20

pesoTotal = pesoMorango + pesoMaca
subtotal = (precoMaca * precoMorango) + (precoMorango * precoMaca)

if pesoTotal > 8 or subtotal > 25:
    desconto = subtotal * 0.10
else: 
    desconto = 0

totalPagar = subtotal - desconto

print(f"Peso das maçãs (em kg): {pesoMaca}")
print(f"Peso dos morangos (em kg): {pesoMorango}")
print(f"Soma dos pesos (em kg): {pesoTotal}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R${totalPagar:.2f}")