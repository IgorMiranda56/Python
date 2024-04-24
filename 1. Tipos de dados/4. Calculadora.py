# Calculadora
import os

os.system("cls || clear")

primeiroNumero: int
segundoNumero: int

print(" === Solicitando dados === \n")
primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

adicao = primeiroNumero + segundoNumero
subtracao = primeiroNumero - segundoNumero
divisao = primeiroNumero / segundoNumero
multiplicacao = primeiroNumero * segundoNumero

print(" === Exibindo dados === \n")
print(f"Primeiro número: {primeiroNumero}")
print(f"Segundo número: {segundoNumero}")
print(f"Adição: {adicao}")
print(f"Subtração: {subtracao}")
print(f"Divisão: {divisao}")
print(f"Multiplicação: {multiplicacao}")
