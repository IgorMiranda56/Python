import os

numero = int(input("Digite um número: "))

os.system("cls || clear")

for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")