import os
os.system("cls || clear")

par = 0
impar = 0

for i in range(1,6):
    numero = int(input(F"Digite o {i}º número: "))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Quantidade de pares: {par}")
print(f"Quantidade de ímpares: {impar}")
