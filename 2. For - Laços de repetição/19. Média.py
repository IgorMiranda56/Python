import os
os.system("cls || clear")

soma = 0

for i in range (1, 5):
    nota = float(input(f"Digite sua {i}ª nota: "))
    soma += nota

media = soma / 4

print(f"Média do aluno: {media}")
