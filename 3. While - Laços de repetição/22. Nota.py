import os
os.system("cls || clear")

soma = 0
contador = 0

while True: 
    nota = float(input("Digite sua nota: "))
    contador += 1
    soma += nota

    if contador > 1:
        break
media = soma / contador

print(f"Média: {media}")