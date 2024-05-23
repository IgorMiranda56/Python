import os
os.system("cls || clear")

def cabecalho():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def tabuada(valor1, valor2):
    return valor1 * valor2
cabecalho()
numero = int(input("Digite um número: "))

cabecalho()
for i in range(1, 11):
    resposta = tabuada(numero, i)
    print(f"{numero} x {i} = {resposta}")