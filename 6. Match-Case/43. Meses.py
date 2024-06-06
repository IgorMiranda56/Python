import os
import time

while True:
    opcao = int(input("Digite um número (De 1 a 12): "))
    if opcao > 12 or opcao < 1:
        os.system("cls || clear")
        print("Número inválido.")
    match(opcao):
        case 1:
            mes = "Janeiro"
            break
        case 2:
            mes = "Fevereiro"
            break
        case 3:
            mes = "Março"
            break
        case 4:
            mes = "Abril"
            break
        case 5:
            mes = "Maio"
            break
        case 6:
            mes = "Junho"
            break
        case 7:
            mes = "Julho"
            break
        case 8:
            mes = "Agosto"
            break
        case 9:
            mes = "Setembro"
            break
        case 10:
            mes = "Outubro"
            break
        case 11:
            mes = "Novembro"
            break
        case 12:
            mes = "Dezembro"
            break
        case _:
            time.sleep(2)

print(f"Mês: {mes}")