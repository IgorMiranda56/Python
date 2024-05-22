import os
os.system("cls || clear")

# Criando uma lista / vetor
notas = []

# Solicitando 3 notas
for i in range(3):
        nota = float(input("Digite sua nota: "))
        notas.append(nota)

# Exibindo as notas        
for i in range(3):
        print(f"Nota: {notas[i]}")