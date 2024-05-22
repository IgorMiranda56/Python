import os
import sys
os.system("cls || clear")

numeros = []
maiorNumero = 0
menorNumero = sys.maxsize

QUANTIDADE_NUMEROS = 5

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    maiorNumero = max(maiorNumero, numero)
    menorNumero = min(menorNumero, numero)

for i, numero in enumerate(numeros):
    print(f"{i+1}º Números: {numero}")
    
print(f"Maior números: {maiorNumero}")
print(f"Menor números: {menorNumero}")