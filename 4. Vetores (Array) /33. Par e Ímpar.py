import os
os.system("cls || clear")

numeros = []
QUANTIDADE_NUMERO = 6
par = 0
impar = 0

for i in range(QUANTIDADE_NUMERO):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
    if numero % 2 == 0:
        par += 1
    else: 
        impar += 1

for i, numero in enumerate(numeros):
    print(f"{i+1}º Número: {numero}")

print(f"Quantidade de números pares: {par}")
print(f"Quantidade de números ímpares: {impar}")