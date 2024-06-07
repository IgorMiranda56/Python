import os
import time

prato = ""
valor = 0
while True:
    print("Menu")
    print("1 - Picanha")
    print("2 - Lasanha")
    print("3 - Strogonoff")
    print("4 - Bife acebolado")
    print("5 - Pão com ovo")
    opcao = int(input("Digite um número do menu: "))
    if opcao > 5 or opcao < 1:
         print("Digite um número válido.")
    os.system("cls || clear")
    match(opcao):
        case 1:
            prato = "Picanha"
            valor = 25.00
            break
        case 2:
            prato = "Lasanha"
            valor = 20.00
            break
        case 3:
            prato = "Strogonoff"
            valor = 18.00
            break
        case 4:
            prato = "Bife acebolado"
            valor = 15.00
            break
        case 5:
            prato = "Pão com ovo"
            valor = 5.00
            break
        case _:
            time.sleep(2)

print(f"Prato - {prato}")
print(f"Preço - R${valor}")