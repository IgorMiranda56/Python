# idade mínima
 
import os

os.system("cls || clear")

idade = int(input("Digite uma idade: "))

if idade >= 18 and idade <= 65:
    print("Voto obrigatório.")
else:
    print("O voto não é obigatório.")