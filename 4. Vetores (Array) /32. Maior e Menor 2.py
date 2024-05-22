import os
import sys
os.system("cls || clear")

numeros = []
maiorNumero = 0
menorNumero = sys.maxsize

while True:
        numero = int(input("Digite um número: "))
        if numero < 0:
            print("Número inválido, digite novamente. ")
        elif numero == 0:
            maiorNumero = max(numeros)
            menorNumero = min(numeros)
            break
        else:
             numeros.append(numero)
            

for i, numero in enumerate(numeros):
    print(f"{i+1}º Números: {numero}")
    
print(f"Maior números: {maiorNumero}")
print(f"Menor números: {menorNumero}")