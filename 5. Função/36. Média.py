import os

def cabecalho():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def calculo_media(valor1, valor2):
    resultado = (valor1 + valor2) / 2
    return resultado   
cabecalho()    
primeiroNumero = float(input("Digite seu primeiro número: "))
segundoNumero = float(input("Digite seu segundo número: "))

media = calculo_media(primeiroNumero, segundoNumero)
cabecalho()
print(f"Média: {media}")