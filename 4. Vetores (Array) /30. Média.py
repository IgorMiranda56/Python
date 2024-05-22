import os
os.system("cls || clear")

notas = []
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
        nota = float(input("Digite sua nota: "))
        notas.append(nota)
        soma = sum(notas)

# ForEach - ParaCada
for i, nota in enumerate(notas):
        print(f"{i+1}º Nota: {nota}")
"""
# ForEach 
for nota in notas
        print(f"Nota: (nota)")
"""

media = soma / QUANTIDADE_NOTAS
print(f"Média: {media}")