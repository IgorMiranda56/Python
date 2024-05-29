import os
import time

#Limpar terminal.
os.system("cls || clear")

#Inicializar variável.
resultado = 0

#Solicitar dados para o usuário.

while True:
    os.system("cls || clear")
    primeiroNumero = int(input("Digite o primeiro número:"))
    operador = input("Digite um operador: (+,-,/,*):")
    segundoNumero = int(input("Digite o segundo número:"))
    if operador != '/' or operador != '*' or operador != '-' or operador != '+':
        print("Digite um operador válido!")
        match(operador):
            case '+':
                resultado = primeiroNumero + segundoNumero
                break
            case '-':
                resultado = primeiroNumero - segundoNumero
                break
            case '/':
                resultado = primeiroNumero / segundoNumero
                break
            case '*':
                resultado = primeiroNumero * segundoNumero
                break
            case _:           
                print("Operador inválido.")
                time.sleep(2)
        
print(f"Resultado: {resultado}")