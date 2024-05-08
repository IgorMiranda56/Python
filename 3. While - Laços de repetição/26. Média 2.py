import os

os.system("cls || clear")

soma = 0 
contador = 0
"""
while True: 
    nota = float(input(f"Digite sua nota: "))
    contador += 1
    soma += nota
    if nota > 0:
        nota = float(input(f"Digite sua nota: "))
    else:
        media = soma / contador
        print(f"Média: {media}")
        break
"""
while nota > 0:
    nota = float(input(f"Digite sua nota: "))
    if nota >= 0:
        contador+= 1
        soma += nota

media = soma / contador

print("\nMédia: %.1f", media)