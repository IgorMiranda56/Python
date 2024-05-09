import os
import time
os.system("clear")

par = 0
somaPar = 0
somaimpar = 0
impar = 0
mediaPar = 0
mediaImpar = 0
contadorGeral = 0

while True:
    numero = int(input("Digite um numero: "))

    if numero > 0:
        contadorGeral += 1
        if numero % 2 == 0:
            par += 1
            somaPar += numero
            mediaPar = somaPar / par
        else:
            impar += 1
            somaimpar += numero
    else:
        if contadorGeral == 0:
            print("Digite novamente. ")
            time.sleep(1)
            os.system("clear")
        else:
            if numero == 0:
                break

somaGeral = somaPar + somaimpar
mediaGeral = somaGeral / contadorGeral

print(f"Quantidade de pares: {par}")
print(f"Quantidade de ímpares: {impar}")
print(f"Média dos números pares: {mediaPar}")
print(f"Média Geral: {mediaGeral}")
