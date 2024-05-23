import os
os.system("cls || clear")
def calculo_media(valor1, valor2):
    resultado = (valor1 + valor2) / 2
    return resultado   
    
primeiroNumero = float(input("Digite seu primeiro número: "))
segundoNumero = float(input("Digite seu segundo número: "))

media = calculo_media(primeiroNumero, segundoNumero)
print(f"Média: {media}")