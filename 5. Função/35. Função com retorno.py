import os
os.system("cls || clear")

# Função com retorno.
def somar(valor1, valor2):
    resultado = valor1 + valor2
    return resultado
def subtrair(valor1, valor2):
    resultado = valor1 - valor2
    return resultado
def dividir(valor1, valor2):
    return valor1 / valor2
def multiplicar(valor1, valor2):
    return valor1 * valor2

primeiroNumero = int(input("Digite seu primeiro número: "))
segundoNumero = int(input("Digite seu segundo número: "))

soma = somar(primeiroNumero, segundoNumero)
subtracao = subtrair(primeiroNumero, segundoNumero)
divisao = dividir(primeiroNumero, segundoNumero)
multiplicacao = multiplicar(primeiroNumero, segundoNumero)

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Divisão: {divisao}")
print(f"Multiplicação: {multiplicacao}")



