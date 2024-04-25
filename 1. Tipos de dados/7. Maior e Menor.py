# MAIOR e MENOR número
import os

os.system("cls || clear")

print(" === Solicitando dados === \n")
primeiroNumero = int(input("Digite o 1º número: "))
segundoNumero = int(input("Digite o 2º número: "))

soma = primeiroNumero + segundoNumero
media = soma / 2
multiplicacao = primeiroNumero * segundoNumero

print(" === Exibindo resultado === \n")
print(f"Soma: {soma}")
print(f"Multiplicação: {multiplicacao}")
print(f"Média: {media}")

if primeiroNumero > segundoNumero:
    print(f"Maior número: {primeiroNumero}")
elif segundoNumero > primeiroNumero:
    print(f"Maior número: {segundoNumero}")

if primeiroNumero < segundoNumero:
    print(f"Menor número: {primeiroNumero}")
elif segundoNumero < primeiroNumero:
    print(f"Menor número: {segundoNumero}")

if primeiroNumero == segundoNumero:
    print(f"Os números são iguais.")
"""
maiorNumero = max(primeiroNumero, segundoNumero)
menorNumero = min(primeiroNumero, segundoNumero)

if primeiroNumero > segundoNumero:
    maiorNumero = primeiroNumero
else:
    maiorNumero = segundoNumero

if primeiroNumero < segundoNumero:
    menorNumero = primeiroNumero
else:
    menorNumero = segundoNumero
"""

