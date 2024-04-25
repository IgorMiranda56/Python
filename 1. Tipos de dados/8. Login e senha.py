# LOGIN e SENHA

import os

os.system("cls || clear")

login = str(input("Digite seu e-mail: "))
senha = int(input("Digite sua senha: "))

if login == "igor" and senha == 123:
    print("Bem vindo!")
else:
    print("Login ou senha inválidos.")