import os

os.system("cls || clear")

QUANTIDADE_NOTAS = 3
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True: 
        nota = float(input(f"Digite sua {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("Nota inválida. Tente novamente. \n")
        else:
            soma += nota    
            break

media = soma / QUANTIDADE_NOTAS

print(f"Média: {media}")
if media >= 7:
    print("Aprovado.")
elif media >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")