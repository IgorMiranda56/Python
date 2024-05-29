import os

opcao = int(input("Digite um número que representa um dia da semana:"))
os.system("cls || clear")
match(opcao):
        case 1:
            dia = "Domingo"
        case 2:
            dia = "Segunda-feira"
        case 3:
            dia = "Terça-feira"
        case 4:
            dia = "Quarta-feira"
        case 5:
            dia = "Quinta-feira"
        case 6:
            dia = "Sexta-feira"
        case 7:
            dia = "Sábado"
        case _:
            print("Digite um número válido")

if dia == "Domingo" or dia == "Sábado":
    print(f"Dia da semana: {dia}")
    print("Final de semana.")
else:
    print(f"Dia da semana: {dia}")
    print("Dia útil.")