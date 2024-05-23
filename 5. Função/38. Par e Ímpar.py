import os

def cabecalho():
    os.system("cls || clear")
    print("=============")
    print("====SENAI====")
    print("=============")

quantidadePar = 0
quantidadeImpar = 0
lista_numeros = []
QUANTIDADE_NUMEROS = 6

def verificarPar(numeros):
    pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1    
    return pares
def verificarImpar(numeros):
    impares = 0
    for  numero in numeros:
        if numero % 2 != 0:
            impares += 1
    return impares

cabecalho()
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

quantidadePar = verificarPar(lista_numeros)
quantidadeImpar = verificarImpar(lista_numeros)

cabecalho()
print(f"Quantidade de números pares: {quantidadePar}")
print(f"Quantidade de números ímpares: {quantidadeImpar}")