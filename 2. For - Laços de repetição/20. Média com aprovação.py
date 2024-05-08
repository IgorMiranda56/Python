import os
os.system("cls || clear")

soma = 0

for i in range (1, 4):
    nota = float(input(f"Digite sua {i}ª nota: "))
    soma += nota

media = soma / 3

print(f"Média do aluno: {media}")
if media >= 7:
    print("Aprovado.")
elif media >= 4:
    print("Recuperação.")
else:
    print("Reprovado.")